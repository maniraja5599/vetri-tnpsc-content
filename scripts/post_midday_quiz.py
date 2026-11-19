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
        print("Error: No bot token found.")
        return

    chat_id = "@VetriTNPSCApp"
    playstore_url = "https://play.google.com/store/apps/details?id=com.vetritnpsc.app"

    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        content = json.load(f)

    with open(TRACKER_FILE, "r", encoding="utf-8") as f:
        posted = set(json.load(f))

    target_ids = ["ta0056", "ta0057"]
    newly_posted = []

    for q in content.get("questions", []):
        if q["id"] in target_ids and q["id"] not in posted:
            poll_payload = {
                "chat_id": chat_id,
                "question": q["q"][:300],
                "options": [{"text": str(o)[:100]} for o in q["o"]],
                "type": "quiz",
                "correct_option_id": q["a"],
                "explanation": (q.get("e", "") + " | Play Store-ல் 'Vetri TNPSC' Install செய்யவும்!")[:200],
                "is_anonymous": True,
            }

            req = urllib.request.Request(
                f"https://api.telegram.org/bot{token}/sendPoll",
                data=json.dumps(poll_payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            try:
                with urllib.request.urlopen(req) as resp:
                    res_data = json.loads(resp.read().decode())
                    poll_id = res_data.get("result", {}).get("message_id")
                    print(f"✅ Published {q['id']} successfully! Poll Message ID: {poll_id}")
                    newly_posted.append(q["id"])
                    posted.add(q["id"])
            except Exception as e:
                print(f"❌ Failed to post {q['id']}: {e}")

            time.sleep(2)

    if newly_posted:
        promo_text = (
            "🎯 *TNPSC Group 4 & VAO 2026 - பொதுத்தமிழ் சிறப்புப் பயிற்சி*\n\n"
            "📖 *சமச்சீர் பாடப்புத்தகம் (6 - 12 ஆம் வகுப்பு)* வினாக்கள் தினமும் இலவசமாக எழுத:\n\n"
            "📲 *Vetri TNPSC Android செயலியை உடனே Play Store-ல் பதிவிறக்கம் செய்யுங்கள்!*\n"
            "✨ *முக்கிய சிறப்பம்சங்கள்:*\n"
            "• 100+ பாடவாரியான மாதிரித் தேர்வுகள்\n"
            "• உடனடி விடைகள் & விரிவான விளக்கங்கள்\n"
            "• முழுமையான இலவச பயன்பாடு\n\n"
            "👇 *இப்போதே கீழே உள்ள பட்டனை கிளிக் செய்து இன்ஸ்டால் செய்யுங்கள்!*"
        )

        reply_markup = {
            "inline_keyboard": [
                [
                    {
                        "text": "📲 Install Vetri TNPSC (Play Store)",
                        "url": playstore_url,
                    }
                ],
                [
                    {
                        "text": "🚀 Forward to TNPSC Group",
                        "url": "https://t.me/share/url?url=https://t.me/VetriTNPSCApp&text=TNPSC%20Group%204%20தினசரி%20மாதிரி%20தேர்வு%20எழுத%20சேருங்கள்!",
                    }
                ],
            ]
        }

        msg_payload = {
            "chat_id": chat_id,
            "text": promo_text,
            "parse_mode": "Markdown",
            "reply_markup": reply_markup,
        }

        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=json.dumps(msg_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req) as resp:
                print("✅ Telegram promo announcement with direct Install CTA broadcasted!")
        except Exception as e:
            print(f"❌ Promo message failed: {e}")

        # Save updated posted IDs
        with open(TRACKER_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(posted)), f, ensure_ascii=False, indent=2)
        print(f"Updated tracker file. Total posted quizzes: {len(posted)}")

if __name__ == "__main__":
    run()
