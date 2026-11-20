#!/usr/bin/env python3
"""
Make daily Instagram/WhatsApp quiz carousel images for Vetri TNPSC.

Each day = 2 images (1080x1350):
  posts/<date>_1.png  question + 4 options
  posts/<date>_2.png  correct answer + explanation + app call-to-action
plus posts/posts.json with captions, ready for Metricool scheduling.

Tamil text is rendered by Microsoft Edge (headless) because Pillow on this
machine has no complex-script shaping. Run:
  python scripts/make_daily_posts.py --days 30 --start 2026-11-21
"""
import argparse, datetime as dt, html, json, random, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_QUESTIONS = ROOT.parent / "Vetri TNPSC" / "assets" / "data" / "questions.json"
OUT = ROOT / "posts"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PLAY = "https://play.google.com/store/apps/details?id=com.vetritnpsc.app"

SUBJECT_TA = {
    "tamil": "பொதுத்தமிழ்", "ta": "பொதுத்தமிழ்", "kural": "திருக்குறள்",
    "history": "வரலாறு", "polity": "இந்திய அரசியலமைப்பு", "geography": "புவியியல்",
    "science": "அறிவியல்", "tn": "தமிழ்நாடு நிர்வாகம்", "aptitude": "திறனறிவு",
}
TAMILISH = {"tamil", "ta", "kural"}

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:'Nirmala UI','Latha',sans-serif;color:#1d1640;
 background:linear-gradient(160deg,#4b2bd6 0%,#7b3fe4 55%,#a855f7 100%);
 display:flex;flex-direction:column;padding:56px 60px}
.top{display:flex;justify-content:space-between;align-items:center;color:#fff}
.brand{font-size:40px;font-weight:700;letter-spacing:.5px}
.day{font-size:30px;background:rgba(255,255,255,.18);padding:10px 24px;border-radius:40px}
.chip{align-self:flex-start;margin-top:34px;background:#ffd23f;color:#3a2a00;
 font-size:32px;font-weight:700;padding:10px 28px;border-radius:40px}
.card{background:#fff;border-radius:36px;margin-top:28px;padding:48px 48px 40px;
 box-shadow:0 18px 50px rgba(20,0,60,.35);flex:1;display:flex;flex-direction:column}
.q{font-size:QSIZEpx;line-height:1.45;font-weight:700}
.opts{margin-top:30px;display:flex;flex-direction:column;gap:16px}
.o{display:flex;align-items:center;gap:22px;font-size:OSIZEpx;border:3px solid #e4defa;
 border-radius:24px;padding:14px 26px;background:#f8f6ff}
.o b{flex:none;width:58px;height:58px;border-radius:50%;background:#4b2bd6;color:#fff;
 display:flex;align-items:center;justify-content:center;font-size:30px}
.o.ok{border-color:#16a34a;background:#e9f9ef}.o.ok b{background:#16a34a}
.o.dim{opacity:.38}
.exp{margin-top:24px;font-size:29px;line-height:1.45;background:#fff8db;border-radius:22px;padding:20px 26px}
.foot{margin-top:26px;color:#fff;text-align:center;font-size:34px;line-height:1.45}
.foot .big{font-size:42px;font-weight:700}
"""


def load_questions():
    d = json.loads(APP_QUESTIONS.read_text(encoding="utf-8"))
    qs = d["questions"] if isinstance(d, dict) else d
    # Evergreen only: dated current affairs go stale, keep 4 options + explanation.
    return [q for q in qs if q.get("s") != "ca" and len(q.get("o", [])) == 4 and q.get("e")]


def pick(qs, n, seed):
    rnd = random.Random(seed)
    tam = [q for q in qs if q["s"] in TAMILISH]
    gs = [q for q in qs if q["s"] not in TAMILISH]
    rnd.shuffle(tam); rnd.shuffle(gs)
    out = []
    for i in range(n):  # ~70:30 Tamil : General Studies (best Telegram engagement)
        src = gs if (i % 10 in (2, 5, 8) and gs) else (tam or gs)
        out.append(src.pop())
    return out


def sizes(q):
    ql = len(q["q"]); ol = max(len(o) for o in q["o"])
    qs = 50 if ql < 45 else 44 if ql < 75 else 38
    os_ = 36 if ol < 22 else 32
    return qs, os_


def page(q, day, answer):
    qs, os_ = sizes(q)
    css = CSS.replace("QSIZE", str(qs)).replace("OSIZE", str(os_))
    letters = "ABCD"
    opts = []
    for i, o in enumerate(q["o"]):
        cls = "o" + ((" ok" if i == q["a"] else " dim") if answer else "")
        opts.append(f'<div class="{cls}"><b>{letters[i]}</b><span>{html.escape(o)}</span></div>')
    subj = SUBJECT_TA.get(q["s"], "பொது அறிவு")
    if answer:
        body = (f'<div class="q">{html.escape(q["q"])}</div><div class="opts">{"".join(opts)}</div>'
                f'<div class="exp">✅ {html.escape(q["e"])}</div>')
        foot = ('<div class="big">தினமும் பயிற்சிக்கு: Vetri TNPSC app</div>'
                'Play Store-ல் இலவசம் • link bio-வில்')
    else:
        body = f'<div class="q">{html.escape(q["q"])}</div><div class="opts">{"".join(opts)}</div>'
        foot = ('<div class="big">உங்கள் பதில் என்ன? 👇 Comment செய்யுங்கள்</div>'
                'சரியான பதில் அடுத்த slide-ல் ➡️')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="top"><div class="brand">✔ Vetri TNPSC</div><div class="day">இன்றைய கேள்வி #{day}</div></div>
<div class="chip">{subj}</div><div class="card">{body}</div><div class="foot">{foot}</div></body></html>"""


def render(html_text, png):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_text); src = Path(f.name)
    try:
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1", "--window-size=1080,1350",
                        f"--screenshot={png}", src.as_uri()],
                       check=True, capture_output=True, timeout=60)
    finally:
        src.unlink(missing_ok=True)


def caption(q, day):
    subj = SUBJECT_TA.get(q["s"], "பொது அறிவு")
    return (f"இன்றைய TNPSC கேள்வி #{day} | {subj}\n\n{q['q']}\n\n"
            "உங்கள் பதிலை comment-ல் சொல்லுங்கள் 👇 சரியான பதில் 2-வது slide-ல்.\n\n"
            "தினமும் Daily Challenge, Mock Test, பொதுத்தமிழ் பயிற்சிக்கு Vetri TNPSC app (Play Store, இலவசம்) – link bio-வில்.\n\n"
            "#TNPSC #TNPSCGroup4 #Group4 #TNPSCGroup2 #VAO #பொதுத்தமிழ் #TNPSCTamil #TamilNadu #GovtExam #VetriTNPSC")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--start", default=(dt.date.today() + dt.timedelta(days=1)).isoformat())
    ap.add_argument("--first-number", type=int, default=1)
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    start = dt.date.fromisoformat(a.start)
    chosen = pick(load_questions(), a.days, a.seed)
    manifest = []
    for i, q in enumerate(chosen):
        day_no = a.first_number + i
        date = (start + dt.timedelta(days=i)).isoformat()
        p1, p2 = OUT / f"{date}_1.png", OUT / f"{date}_2.png"
        render(page(q, day_no, False), p1)
        render(page(q, day_no, True), p2)
        manifest.append({"date": date, "number": day_no, "question_id": q["id"],
                         "images": [f"posts/{p1.name}", f"posts/{p2.name}"], "caption": caption(q, day_no)})
        print(f"{date}  #{day_no}  {q['id']}", flush=True)
    (OUT / "posts.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done: {len(manifest)} days -> {OUT}")


if __name__ == "__main__":
    sys.exit(main())
