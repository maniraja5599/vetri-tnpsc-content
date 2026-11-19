import json
import os
import time
import urllib.parse
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER_FILE = os.path.join(REPO_ROOT, "scripts", "posted_quiz_ids.json")
CONTENT_FILE = os.path.join(REPO_ROOT, "content.json")

def get_token():
    token = None
    env_file = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    token = line.strip().split("=", 1)[1].strip("\"'")
    if not token:
        token = os.environ.get("TELEGRAM_BOT_TOKEN")
    return token

def run():
    token = get_token()
    if not token:
        print("No bot token")
        return

    chat_id = "@VetriTNPSCApp"
    playstore_url = "https://play.google.com/store/apps/details?id=com.vetritnpsc.app"

    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        content = json.load(f)

    with open(TRACKER_FILE, "r", encoding="utf-8") as f:
        posted = set(json.load(f))

    target_ids = ["ta0054", "ta0055"]
    newly_posted = []

    for q in content.get("questions", []):
        if q["id"] in target_ids and q["id"] not in posted:
            poll_payload = {
                "chat_id": chat_id,
                "question": q["q"][:300],
                "options": [{"text": str(o)[:100]} for o in q["o"]],
                "type": "quiz",
                "correct_option_id": q["a"],
                "explanation": (q.get("e", "") + " | Play Store-ல் 'Vetri TNPSC' Install செய்யுங்கள்!")[:200],
                "is_anonymous": True,
            }
            try:
                res = urllib.request.urlopen(
                    urllib.request.Request(
                        f"https://api.telegram.org/bot{token}/sendPoll",
                        data=json.dumps(poll_payload).encode("utf-8"),
                        headers={"Content-Type": "application/json"}
                    )
                )
                res_data = json.loads(res.read().decode("utf-8"))
                print(f"Posted poll ID: {res_data['result']['message_id']} for {q['id']}")
                newly_posted.append(q["id"])
                posted.add(q["id"])
                time.sleep(2)
            except Exception as e:
                print(f"Error on poll {q['id']}:", e)

    if newly_posted:
        share_text = "🎯 TNPSC Group 4 & 2 பொதுத்தமிழ் மாதிரி வினாடி வினா! உடனே Play Store-ல் 'Vetri TNPSC' Install செய்ய: "
        share_url = "https://t.me/share/url?" + urllib.parse.urlencode({
            "url": playstore_url,
            "text": share_text
        })

        promo_text = (
            "🎯 <b>இன்றைய சமச்சீர் பொதுத்தமிழ் மாதிரித் தேர்வு!</b>\n\n"
            "⏱️ 123+ மாதிரி வினாக்கள் & OMR Timer-உடன் பயிற்சி பெற Vetri TNPSC செயலியை உடனே Install செய்யுங்கள்:\n\n"
            f"📲 <b>Play Store:</b> {playstore_url}\n"
            "🌐 <b>Web App:</b> https://vetri-tnpsc-content.vercel.app\n\n"
            "💡 இந்த வினாடி வினாவை உங்கள் நண்பர்கள் மற்றும் Study குரூப்களில் தவறாமல் பகிருங்கள்! 👇"
        )
        markup = {
            "inline_keyboard": [
                [
                    {"text": "📲 Google Play Store-ல் Install செய்", "url": playstore_url}
                ],
                [
                    {"text": "🚀 Study குரூப்களில் பகிருங்கள் (1-Tap Share)", "url": share_url}
                ],
                [
                    {"text": "🌐 Browser-ல் Mock Test எழுத", "url": "https://vetri-tnpsc-content.vercel.app"}
                ]
            ]
        }
        try:
            res = urllib.request.urlopen(
                urllib.request.Request(
                    f"https://api.telegram.org/bot{token}/sendMessage",
                    data=json.dumps({
                        "chat_id": chat_id,
                        "text": promo_text,
                        "parse_mode": "HTML",
                        "reply_markup": markup
                    }).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
            )
            print("Sent promo message with buttons!")
        except Exception as e:
            print("Error on promo:", e)

        with open(TRACKER_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(posted)), f, ensure_ascii=False, indent=2)
        print(f"Updated tracker with {newly_posted}")

if __name__ == "__main__":
    run()
