"""Send one push alert to every app install when content.json gains news or
questions.

Usage: python scripts/notify_push.py OLD_content.json NEW_content.json [--dry-run]

- New news item(s)  -> "📰 <first new title>", opens the News screen.
- Else new questions -> "🆕 N new questions added", opens them.
- Nothing new        -> no message.

Sends to the Firebase Cloud Messaging topic "all" of project vetri-tnpsc.
Credentials: keyless Workload Identity Federation in GitHub Actions
(google-github-actions/auth sets GOOGLE_APPLICATION_CREDENTIALS), or a
FIREBASE_SERVICE_ACCOUNT JSON key as a fallback. Without either the script
prints what it would send and exits 0, so it never fails a merge.
"""

import json
import os
import sys

PROJECT_ID = "vetri-tnpsc"
TOPIC = "all"


def load(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def build_message(old, new):
    old_news = [json.dumps(n, sort_keys=True) for n in old.get("news", [])]
    fresh_news = [
        n for n in new.get("news", []) if json.dumps(n, sort_keys=True) not in old_news
    ]
    if fresh_news:
        first = fresh_news[0]
        more = f" (+{len(fresh_news) - 1} more)" if len(fresh_news) > 1 else ""
        return {
            "title": f"📰 {first['title']}"[:110],
            "body": (first.get("body", "") + more)[:230],
            "target": "news",
        }
    old_ids = {q["id"] for q in old.get("questions", [])}
    added = [q for q in new.get("questions", []) if q["id"] not in old_ids]
    if added:
        n = len(added)
        ca = sum(1 for q in added if q.get("s") == "ca")
        kind = "current affairs " if ca == n else ""
        return {
            "title": f"🆕 {n} new {kind}question{'s' if n > 1 else ''} added",
            "body": "Practise them now in Vetri TNPSC.",
            "target": "new_questions",
        }
    return None


SCOPES = ["https://www.googleapis.com/auth/firebase.messaging"]


def credentials():
    """Keyless first: in GitHub Actions, google-github-actions/auth
    (Workload Identity Federation) sets GOOGLE_APPLICATION_CREDENTIALS to a
    short-lived config, no secret involved. FIREBASE_SERVICE_ACCOUNT (a JSON
    key in a secret) is only a fallback. Returns None if neither is set."""
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        import google.auth

        creds, _ = google.auth.default(scopes=SCOPES)
        return creds
    sa = os.environ.get("FIREBASE_SERVICE_ACCOUNT", "").strip()
    if sa:
        from google.oauth2 import service_account

        return service_account.Credentials.from_service_account_info(
            json.loads(sa), scopes=SCOPES
        )
    return None


def send(msg, creds):
    # Imported here so --dry-run and tests work without these packages.
    from google.auth.transport.requests import AuthorizedSession

    session = AuthorizedSession(creds)
    body = {
        "message": {
            "topic": TOPIC,
            "notification": {"title": msg["title"], "body": msg["body"]},
            "data": {"target": msg["target"]},
            "android": {
                "priority": "high",
                "ttl": "86400s",
                # One alert per kind: a newer one replaces an unread older one.
                "collapse_key": msg["target"],
                "notification": {"channel_id": "updates", "tag": msg["target"]},
            },
        }
    }
    r = session.post(
        f"https://fcm.googleapis.com/v1/projects/{PROJECT_ID}/messages:send",
        json=body,
        timeout=30,
    )
    if r.status_code != 200:
        print(f"FCM error {r.status_code}: {r.text[:500]}")
        return False
    print(f"Sent: {r.json().get('name')}")
    return True


TEST_MESSAGE = {
    "title": "✅ Vetri TNPSC test alert",
    "body": "Push alerts are working. Tap to open the News screen.",
    "target": "news",
}


def main(argv):
    if "--test" in argv:
        # Manual check from the Actions tab: sends one fixed alert.
        msg = TEST_MESSAGE
    else:
        args = [a for a in argv if not a.startswith("--")]
        if len(args) != 2:
            print(__doc__)
            return 2
        msg = build_message(load(args[0]), load(args[1]))
    if msg is None:
        print("Nothing new: no push sent.")
        return 0
    print(f"Push: {msg['title']} | {msg['body']} -> {msg['target']}")
    if "--dry-run" in argv:
        return 0
    creds = credentials()
    if creds is None:
        print("No Google credentials (keyless auth or FIREBASE_SERVICE_ACCOUNT): not sending.")
        return 0
    return 0 if send(msg, creds) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
