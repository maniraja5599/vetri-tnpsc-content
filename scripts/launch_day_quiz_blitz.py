import os
import json
import time
import urllib.request
import urllib.parse

def run_blitz():
    token = None
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    token = line.strip().split("=", 1)[1].strip("\"'")

    if not token:
        print("No bot token")
        return

    chat_id = "@VetriTNPSCApp"

    with open("content.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Pick 3 fresh unposted or high impact questions
    questions = data.get("questions", [])
    
    # Load posted tracker
    tracker_path = os.path.join("scripts", "posted_quiz_ids.json")
    posted = set()
    if os.path.exists(tracker_path):
        with open(tracker_path, "r", encoding="utf-8") as f:
            posted = set(json.load(f))

    unposted = [q for q in questions if q.get("id") not in posted and q.get("s") == "ta"]
    if len(unposted) < 3:
        unposted = [q for q in questions if q.get("s") == "ta"]

    selected = unposted[:3]

    header_text = (
        "🔥 <b>LAUNCH DAY SPECIAL MOCK TEST — 3 வினாக்கள் சவால்!</b> 🎯\n\n"
        "அனைத்து TNPSC ஆஸ்பிரண்ட்ஸும் கீழே உள்ள வினாக்களுக்கு உங்கள் சரியான விடைகளை உடனே பதிவு செய்யுங்கள்! 👇"
    )

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps({"chat_id": chat_id, "text": header_text, "parse_mode": "HTML"}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)
    time.sleep(1)

    newly_posted = []
    for q in selected:
        opts = [{"text": str(o)[:100]} for o in q.get("o", [])]
        poll_payload = {
            "chat_id": chat_id,
            "question": q.get("q", "")[:300],
            "options": opts,
            "type": "quiz",
            "correct_option_id": q.get("a", 0),
            "explanation": (q.get("e", "") + " | Vetri TNPSC App")[:200],
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
            time.sleep(2)
        except urllib.error.HTTPError as e:
            print(f"HTTPError on poll {q['id']}: {e.code} - {e.read().decode('utf-8')}")
            break

    # Follow-up viral CTA
    share_text = "🎯 TNPSC Group 4 & 2 பொதுத்தமிழ் & நடப்பு நிகழ்வுகள் டெஸ்ட் எழுத Play Store-ல் 'Vetri TNPSC' ஆப் வந்துவிட்டது! உடனே Install செய்ய: "
    share_url = "https://t.me/share/url?" + urllib.parse.urlencode({
        "url": "https://play.google.com/store/apps/details?id=com.vetritnpsc.app",
        "text": share_text
    })

    cta_payload = {
        "chat_id": chat_id,
        "text": (
            "🏆 <b>முழுமையான 50 வினாக்கள் OMR மாதிரித் தேர்வை எழுத ஆப் தயார்!</b>\n\n"
            "📲 <b>Play Store Link:</b>\nhttps://play.google.com/store/apps/details?id=com.vetritnpsc.app\n\n"
            "👥 உங்கள் TNPSC Telegram & WhatsApp நண்பர்கள் குரூப்களில் இந்த வினாடி வினாவைப் பகிருங்கள்! 👇"
        ),
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "📲 Google Play Store-ல் Install செய்", "url": "https://play.google.com/store/apps/details?id=com.vetritnpsc.app"}],
                [{"text": "🚀 WhatsApp / Telegram குரூப்களில் பகிர (1-Tap)", "url": share_url}]
            ]
        }
    }
    urllib.request.urlopen(
        urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=json.dumps(cta_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
    )
    print("Blitz finished and CTA sent!")

    # Update tracker
    if os.path.exists(tracker_path):
        with open(tracker_path, "r", encoding="utf-8") as f:
            cur = json.load(f)
        cur.extend(newly_posted)
        with open(tracker_path, "w", encoding="utf-8") as f:
            json.dump(sorted(list(set(cur))), f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    run_blitz()
