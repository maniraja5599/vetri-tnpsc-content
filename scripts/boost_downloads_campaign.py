#!/usr/bin/env python3
"""
Direct Play Store App Download Boost Campaign for Vetri TNPSC.
Broadcasts high-urgency mock test challenges and premium quiz polls
to Telegram channel (@VetriTNPSCApp) to convert subscribers into active app installs.
"""

import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime

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

def run_boost():
    token = get_token()
    if not token:
        print("No telegram bot token")
        return

    chat_id = "@VetriTNPSCApp"
    playstore_url = "https://play.google.com/store/apps/details?id=com.vetritnpsc.app"

    # 1. High-Converting App Download Challenge Announcement
    share_text = "🎯 TNPSC Group 4 & 2 பொதுத்தமிழ் 50 வினாக்கள் OMR மாதிரித் தேர்வு எழுத Play Store-ல் 'Vetri TNPSC' ஆப் வந்துவிட்டது! உடனே Install செய்ய: "
    share_url = "https://t.me/share/url?" + urllib.parse.urlencode({
        "url": playstore_url,
        "text": share_text
    })

    challenge_text = (
        "🔥 <b>இன்றைய 50 வினாக்கள் OMR மாதிரித் தேர்வு ஆப்பில் தயார்!</b> 🎯📚\n\n"
        "அன்பான TNPSC தேர்வர்களே!\n"
        "இன்று நாம் புதிதாக சேர்த்துள்ள 10-ஆம் மற்றும் 11-ஆம் வகுப்பு சமச்சீர் பொதுத்தமிழ் வினாக்களுடன் கூடிய முழு மாதிரித் தேர்வு <b>Vetri TNPSC</b> செயலியில் தயாராக உள்ளது.\n\n"
        "⚡ <b>ஆப்பில் உங்கள் பயிற்சிகள்:</b>\n"
        "• ⏱️ Real Exam 15-வினாடி Timer OMR தேர்வு\n"
        "• 📊 உடனடியாக தோன்றும் மதிப்பெண் & விரிவான விடைக்குறிப்பு\n"
        "• 📚 123+ உயர்தர சமச்சீர் கல்வி வினா வங்கி\n"
        "• 💯 100% இலவசப் பயன்பாடு (No Ads disturbance)\n\n"
        "📲 <b>கீழே உள்ள பட்டனைத் தட்டி இப்போதே Play Store-ல் Install செய்து உங்கள் பயிற்சியைத் தொடங்குங்கள்! 👇</b>"
    )

    markup = {
        "inline_keyboard": [
            [
                {"text": "📲 Google Play Store-ல் Install செய்", "url": playstore_url}
            ],
            [
                {"text": "⭐ Play Store-ல் 5-Star Rating அளித்து ஆதரிக்க", "url": playstore_url}
            ],
            [
                {"text": "🚀 Study குரூப்களில் பகிருங்கள் (1-Tap Share)", "url": share_url}
            ]
        ]
    }

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps({
            "chat_id": chat_id,
            "text": challenge_text,
            "parse_mode": "HTML",
            "reply_markup": markup
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        res = urllib.request.urlopen(req)
        res_data = json.loads(res.read().decode("utf-8"))
        print(f"Broadcast sent! Message ID: {res_data['result']['message_id']}")
    except Exception as e:
        print("Broadcast error:", e)

    time.sleep(2)

    # 2. Post Batch 3 Polls (ta0046, ta0047)
    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        content = json.load(f)

    with open(TRACKER_FILE, "r", encoding="utf-8") as f:
        posted = set(json.load(f))

    target_ids = ["ta0048", "ta0049"]
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
        with open(TRACKER_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(posted)), f, ensure_ascii=False, indent=2)
        print(f"Updated tracker with {newly_posted}")

if __name__ == "__main__":
    run_boost()
