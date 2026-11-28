"""Add verified previous-year (PYQ) questions from pyq/*.json to content.json.

Usage:
  python scripts/add_pyq.py pyq/g4_2025_tamil.json            # dry run
  python scripts/add_pyq.py pyq/g4_2025_tamil.json --write    # update content.json

Rules (same as the "rules" list inside each pyq file):
- Only questions with "status": "verified" are added. "transcribed" means
  typed from the official paper but not yet checked a second time against
  the page image and the official FINAL answer key.
- Questions already in content.json (same id) are skipped, never changed.
- Each question needs: id, s (app subject key), t, q, 4 different options
  in "o", answer index "a" 0-3, explanation "e", and "src".
- Plain text only (no HTML / links), like .github/check.js.

The result goes to main through a normal PR that the owner reviews (the
auto-merge workflow only takes current-affairs PRs).
"""

import datetime
import json
import re
import sys

SUBJECTS = {"tamil", "kural", "history", "polity", "geography", "science",
            "tn", "aptitude", "ca"}
BAD_TEXT = re.compile(r"[<>]|https?://|javascript:|www\.", re.I)


def problems(q):
    out = []
    for k in ("id", "s", "t", "q", "e", "src"):
        if not isinstance(q.get(k), str) or not q[k].strip():
            out.append(f"missing {k}")
    if q.get("s") not in SUBJECTS:
        out.append(f"unknown subject {q.get('s')!r}")
    o = q.get("o")
    if not (isinstance(o, list) and len(o) == 4 and all(isinstance(x, str) and x.strip() for x in o)
            and len(set(o)) == 4):
        out.append("needs 4 different options")
    if not (isinstance(q.get("a"), int) and 0 <= q["a"] <= 3):
        out.append("answer index must be 0-3")
    for v in [q.get("t"), q.get("q"), q.get("e"), *(o or [])]:
        if isinstance(v, str) and (BAD_TEXT.search(v) or len(v) > 400):
            out.append("HTML/link or text over 400 characters")
            break
    return out


def to_content(q):
    """Keep only the fields the app reads, plus src for the record."""
    keep = {k: q[k] for k in ("id", "s", "t", "q", "o", "a", "e", "src")}
    for k in ("qe", "oe"):
        if k in q:
            keep[k] = q[k]
    return keep


def main(argv):
    if not argv or argv[0].startswith("--"):
        print(__doc__)
        return 2
    write = "--write" in argv
    pyq = json.load(open(argv[0], encoding="utf-8-sig"))
    content = json.load(open("content.json", encoding="utf-8-sig"))
    have = {q["id"] for q in content["questions"]}

    add, skipped = [], []
    for q in pyq["questions"]:
        if q.get("status") != "verified":
            skipped.append((q.get("id"), f"status {q.get('status')!r}, not verified"))
            continue
        if q["id"] in have:
            skipped.append((q["id"], "already in content.json"))
            continue
        bad = problems(q)
        if bad:
            skipped.append((q["id"], "; ".join(bad)))
            continue
        add.append(to_content(q))

    print(f"Source: {pyq.get('source')}")
    print(f"To add: {len(add)}")
    for qid, why in skipped:
        print(f"  skip {qid}: {why}")
    if not add:
        return 0
    if not write:
        print("Dry run. Add --write to update content.json.")
        return 0

    content["questions"].extend(add)
    content["version"] = int(content["version"]) + 1
    content["updated"] = datetime.date.today().isoformat()
    with open("content.json", "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"content.json: +{len(add)} questions, version {content['version']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
