#!/usr/bin/env python3
"""
Automated Daily Telegram Quiz Poster for Vetri TNPSC.
Posts fresh questions from content.json to https://t.me/VetriTNPSCApp as interactive Quiz Polls.
"""

import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_FILE = os.path.join(REPO_ROOT, "content.json")
TRACKER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posted_quiz_ids.json")

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "@VetriTNPSCApp")

# Fallback: check local .env file (gitignored) if running locally
if not TELEGRAM_BOT_TOKEN:
    env_file = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    TELEGRAM_BOT_TOKEN = line.strip().split("=", 1)[1].strip("\"'")


def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def send_poll(question_text, options, correct_index, explanation):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPoll"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "question": question_text[:300],
        "options": json.dumps(options[:10]),
        "type": "quiz",
        "correct_option_id": correct_index,
        "explanation": (explanation or "")[:200],
        "is_anonymous": True,
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "disable_web_page_preview": False,
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    content = load_json(CONTENT_FILE, {})
    questions = content.get("questions", [])
    if not questions:
        print("No questions found in content.json")
        return

    posted = set(load_json(TRACKER_FILE, []))

    # Pick unposted questions
    unposted = [q for q in questions if q.get("id") not in posted]

    # If all have been posted, reset tracker to cycle through
    if not unposted:
        print("All questions have been posted. Resetting tracker.")
        posted.clear()
        unposted = questions

    # Smart Selection: Prioritize today's freshest current affairs, then newest unposted
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_unposted = [q for q in unposted if q.get("d") == today_str]
    other_unposted = [q for q in unposted if q.get("d") != today_str]
    other_unposted.reverse()  # Newest questions first

    selected = (today_unposted + other_unposted)[:2]

    newly_posted = []
    for q in selected:
        q_text = q.get("q")
        opts = q.get("o", [])
        correct_idx = q.get("a", 0)
        expl = q.get("e", "")

        if not q_text or not opts or correct_idx >= len(opts):
            continue

        try:
            print(f"Posting question [{q.get('id')}]: {q_text}")
            res = send_poll(q_text, opts, correct_idx, expl)
            if res.get("ok"):
                newly_posted.append(q.get("id"))
                print(f"Success! Poll message ID: {res['result']['message_id']}")
        except Exception as err:
            print(f"Error posting poll: {err}")

    if newly_posted:
        # Send promo message below the daily quizzes
        promo_text = (
            "🎯 TNPSC Group 4 & 2 பொதுத்தமிழ் மற்றும் தினசரி நடப்பு நிகழ்வுகள்!\n\n"
            "⏱️ 50 வினாக்கள் கொண்ட Mock Tests மற்றும் பிழை திருத்தம் (Revise) செய்ய:\n"
            "📲 Vetri TNPSC App-ஐ இலவசமாகப் பதிவிறக்குங்கள்:\n"
            "👉 https://vetri-tnpsc-content.vercel.app\n\n"
            "உங்கள் நண்பர்களுக்கும் இந்த வினாடி வினாவை பகிருங்கள்! 🔥"
        )
        try:
            send_message(promo_text)
            print("Promo message sent successfully.")
        except Exception as err:
            print(f"Error sending promo message: {err}")

        # Update tracker
        posted.update(newly_posted)
        save_json(TRACKER_FILE, sorted(list(posted)))
        print(f"Updated tracker with {len(newly_posted)} new question(s).")


if __name__ == "__main__":
    main()
