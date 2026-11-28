"""Write app usage numbers to Firestore stats/summary for the in-app admin
dashboard (only the owner's account can read it, see firestore.rules).

Usage: python scripts/update_stats.py [--dry-run]

Counts only, no personal data:
- signUps        : Google sign-ins ever (Firebase Auth accounts)
- newToday/new7d : accounts created today (IST) / in the last 7 days
- active7d       : accounts that signed in during the last 7 days
- backups        : users with a cloud backup document
- backups7d      : backups updated in the last 7 days
- contentVersion, questions, lastCaDate : from content.json on main

Credentials: keyless Workload Identity Federation in GitHub Actions
(google-github-actions/auth sets GOOGLE_APPLICATION_CREDENTIALS).
"""

import datetime as dt
import json
import sys

PROJECT = "vetri-tnpsc"
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
FS = f"https://firestore.googleapis.com/v1/projects/{PROJECT}/databases/(default)/documents"


def session():
    import google.auth
    from google.auth.transport.requests import AuthorizedSession

    creds, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    return AuthorizedSession(creds)


def auth_users(s):
    """All Firebase Auth users (createdAt / lastLoginAt in ms)."""
    users, token = [], None
    url = f"https://identitytoolkit.googleapis.com/v1/projects/{PROJECT}/accounts:batchGet"
    while True:
        params = {"maxResults": 1000}
        if token:
            params["nextPageToken"] = token
        r = s.get(url, params=params, timeout=30)
        r.raise_for_status()
        d = r.json()
        users += d.get("users", [])
        token = d.get("nextPageToken")
        if not token:
            return users


def backup_times(s):
    """updatedAt of every users/{uid} backup document."""
    times, token = [], None
    while True:
        params = {"pageSize": 300, "mask.fieldPaths": "updatedAt"}
        if token:
            params["pageToken"] = token
        r = s.get(f"{FS}/users", params=params, timeout=30)
        r.raise_for_status()
        d = r.json()
        for doc in d.get("documents", []):
            ts = doc.get("fields", {}).get("updatedAt", {}).get("timestampValue")
            times.append(ts)
        token = d.get("nextPageToken")
        if not token:
            return times


def ms_to_dt(v):
    return dt.datetime.fromtimestamp(int(v) / 1000, dt.timezone.utc)


def parse_ts(t):
    """Firestore timestamps can carry 9 fraction digits; Python reads 6."""
    import re

    t = re.sub(r"(\.\d{6})\d+", r"\1", t.replace("Z", "+00:00"))
    return dt.datetime.fromisoformat(t)


def summarize(users, backups, content, now):
    today_ist = now.astimezone(IST).date()
    week_ago = now - dt.timedelta(days=7)
    created = [ms_to_dt(u["createdAt"]) for u in users if u.get("createdAt")]
    logins = [ms_to_dt(u["lastLoginAt"]) for u in users if u.get("lastLoginAt")]
    bk = [parse_ts(t) for t in backups if t]
    ca_dates = sorted(q.get("d", "") for q in content["questions"] if q.get("s") == "ca")
    return {
        "signUps": len(users),
        "newToday": sum(1 for c in created if c.astimezone(IST).date() == today_ist),
        "new7d": sum(1 for c in created if c >= week_ago),
        "active7d": sum(1 for x in logins if x >= week_ago),
        "backups": len(backups),
        "backups7d": sum(1 for b in bk if b >= week_ago),
        "contentVersion": int(content.get("version", 0)),
        "questions": len(content["questions"]),
        "lastCaDate": ca_dates[-1] if ca_dates else "",
    }


def to_fields(d, now):
    f = {}
    for k, v in d.items():
        f[k] = {"integerValue": str(v)} if isinstance(v, int) else {"stringValue": v}
    f["updatedAt"] = {"timestampValue": now.strftime("%Y-%m-%dT%H:%M:%SZ")}
    return f


def main(argv):
    content = json.load(open("content.json", encoding="utf-8-sig"))
    now = dt.datetime.now(dt.timezone.utc)
    s = session()
    stats = summarize(auth_users(s), backup_times(s), content, now)
    print(json.dumps(stats, indent=2))
    if "--dry-run" in argv:
        return 0
    r = s.patch(f"{FS}/stats/summary", json={"fields": to_fields(stats, now)}, timeout=30)
    if r.status_code != 200:
        print(f"Firestore error {r.status_code}: {r.text[:300]}")
        return 1
    print("stats/summary updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
