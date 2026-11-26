import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

BUNDLED_PATH = Path(r"c:\Moved_From_E\Projects\Vetri TNPSC\assets\data\questions.json")
REMOTE_PATH = Path(r"c:\Moved_From_E\Projects\vetri-tnpsc-content\content.json")

VALID_SUBJECTS = {
    "tamil", "ta", "kural", "history", "polity",
    "geography", "science", "tn", "aptitude", "ca"
}


def norm_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"^\d+[\.\)]\s*", "", text)
    text = re.sub(r"[^\w\s\u0B80-\u0BFF]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_questions(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("questions", [])


def validate_all(extra_file: Path | None = None) -> int:
    bundled = load_questions(BUNDLED_PATH)
    remote = load_questions(REMOTE_PATH)
    candidates = load_questions(extra_file) if extra_file else []

    all_qs = bundled + ([] if extra_file else [])
    seen_ids: dict[str, str] = {}
    seen_norms: list[tuple[str, str]] = []
    errors: list[str] = []
    warnings: list[str] = []

    def check_one(q: dict, source: str, check_fuzzy: bool = True) -> None:
        qid = q.get("id", "")
        if not qid or not isinstance(qid, str):
            errors.append(f"[{source}] Missing/invalid id: {q}")
            return
        if qid in seen_ids:
            errors.append(f"[{source}] Duplicate id '{qid}' (already in {seen_ids[qid]})")
            return
        seen_ids[qid] = source

        subj = q.get("s", "")
        if subj not in VALID_SUBJECTS:
            errors.append(f"[{qid}] Invalid subject '{subj}'")

        qtext = (q.get("q") or "").strip()
        if len(qtext) < 8:
            errors.append(f"[{qid}] Question text too short: '{qtext}'")

        opts = q.get("o")
        if not isinstance(opts, list) or len(opts) != 4:
            errors.append(f"[{qid}] Options must be a list of 4 items")
            return
        if len({str(o).strip() for o in opts}) != 4:
            errors.append(f"[{qid}] Duplicate options found: {opts}")
        if any(not str(o).strip() for o in opts):
            errors.append(f"[{qid}] Empty option found: {opts}")

        ans = q.get("a")
        if not isinstance(ans, int) or not (0 <= ans < 4):
            errors.append(f"[{qid}] Invalid answer index: {ans}")

        exp = (q.get("e") or "").strip()
        if len(exp) < 5:
            errors.append(f"[{qid}] Explanation missing or too short")

        norm = norm_text(qtext)
        if check_fuzzy:
            for prev_id, prev_norm in seen_norms:
                if norm == prev_norm:
                    errors.append(f"[{qid}] Exact duplicate text of '{prev_id}': {qtext[:60]}")
                    break
                if len(norm) > 20 and len(prev_norm) > 20:
                    ratio = SequenceMatcher(None, norm, prev_norm).ratio()
                    if ratio >= 0.85:
                        warnings.append(
                            f"[{qid}] High similarity ({ratio:.2f}) with '{prev_id}': {qtext[:50]}"
                        )
                        break
        seen_norms.append((qid, norm))

    for q in bundled:
        check_one(q, "bundled", check_fuzzy=True)
    for q in remote:
        if q.get("id") not in seen_ids:
            check_one(q, "remote", check_fuzzy=True)
    for q in candidates:
        check_one(q, "candidate", check_fuzzy=True)

    counts: dict[str, int] = {}
    for q in bundled + [x for x in remote if x.get("id") not in {b["id"] for b in bundled}] + candidates:
        s = "tamil" if q.get("s") == "ta" else q.get("s", "unknown")
        counts[s] = counts.get(s, 0) + 1

    print(f"Total unique IDs checked: {len(seen_ids)}")
    print(f"Subject breakdown: {dict(sorted(counts.items()))}")
    print(f"Errors: {len(errors)} | Fuzzy Warnings (>=0.85): {len(warnings)}")
    for w in warnings[:20]:
        print("  WARN:", w)
    for e in errors[:30]:
        print("  ERR :", e)
    return 1 if errors else 0


if __name__ == "__main__":
    extra = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    sys.exit(validate_all(extra))
