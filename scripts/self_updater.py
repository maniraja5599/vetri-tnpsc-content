#!/usr/bin/env python3
"""
Master Self-Updating Engine for Vetri TNPSC Ecosystem.
Autonomously:
1. Calculates exact testing day (Day X of 14) from anchor date (2026-11-02).
2. Audits content.json questions, unposted count, and posted tracker.
3. Automatically updates PROJECT_MEMORY.md and .agent/skills/vetri-tnpsc-growth-engine/SKILL.md.
4. Ensures the agent and codebase are 100% self-updating without manual prompts.
"""

import os
import json
import subprocess
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_FILE = os.path.join(REPO_ROOT, "content.json")
TRACKER_FILE = os.path.join(REPO_ROOT, "scripts", "posted_quiz_ids.json")
MEMORY_FILE = os.path.join(REPO_ROOT, "PROJECT_MEMORY.md")
SKILL_FILE = os.path.join(REPO_ROOT, ".agent", "skills", "vetri-tnpsc-growth-engine", "SKILL.md")
SHORTS_DIR = os.path.join(REPO_ROOT, "shorts")

# Closed Testing Anchor Date
TESTING_START_DATE = datetime(2026, 11, 2)
TESTING_TOTAL_DAYS = 14


def get_testing_day():
    today = datetime.now()
    delta = (today.date() - TESTING_START_DATE.date()).days + 1
    current_day = max(1, min(delta, TESTING_TOTAL_DAYS))
    days_remaining = max(0, TESTING_TOTAL_DAYS - current_day)
    return current_day, days_remaining


def get_content_stats():
    with open(CONTENT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = data.get("questions", [])
    version = data.get("version", 17)
    updated = data.get("updated", "")

    posted = []
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, "r", encoding="utf-8") as f:
            posted = json.load(f)

    posted_set = set(posted)
    unposted = [q for q in questions if q.get("id") not in posted_set]

    return {
        "version": version,
        "updated": updated,
        "total": len(questions),
        "posted": len(posted),
        "unposted": len(unposted),
        "unposted_tamil": len([q for q in unposted if q.get("s") == "ta"]),
        "unposted_ca": len([q for q in unposted if q.get("s") == "ca"]),
    }


def get_shorts_count():
    if not os.path.exists(SHORTS_DIR):
        return 0
    return len([f for f in os.listdir(SHORTS_DIR) if f.endswith(".mp4")])


def update_project_memory(day, remaining, stats, shorts_count):
    now_str = datetime.now().strftime("%B %d, %Y (%I:%M %p IST)")
    status_headline = f"Day {day} of {TESTING_TOTAL_DAYS}"
    if remaining == 0:
        status_headline += " (🎉 PRODUCTION APPLICATION READY!)"
    else:
        status_headline += f" ({remaining} days until Production Application)"

    content = f"""# Vetri TNPSC Ecosystem - Project Memory & Handoff Summary
**Last Self-Updated:** {now_str} · **Testing Status:** {status_headline}

---

## 🚀 Quick Executive Status
* **Ecosystem:** Vetri TNPSC: Tamil Quiz & VAO (`com.vetritnpsc.app`)
* **Google Play Closed Testing:** **{status_headline}** (15 active human testers, metadata fully approved).
* **Master Question Bank:** **{stats['total']} Total Questions** ({stats['posted']} posted, {stats['unposted']} unposted in reserve: {stats['unposted_tamil']} Tamil + {stats['unposted_ca']} CA).
* **Generated Video Shorts (1080x1920 9:16):** **{shorts_count} Video Shorts ready** in `shorts/`.
* **Web App:** [https://vetri-tnpsc-content.vercel.app](https://vetri-tnpsc-content.vercel.app) (Live 5-Q Test, Gamified Scorecard, WhatsApp Status Share).
* **Telegram Channel:** [@VetriTNPSCApp](https://t.me/VetriTNPSCApp) (86+ subscribers, automated morning 07:55 AM & evening 08:25 PM polls).
* **Telegram Bot:** `@VetriTNPSCQuizBot` (Vercel serverless webhook, Force-Join PDF Funnel, `/invite` Referral Engine, `/tamil` and `/ca` question filters).
* **Lead Magnet PDF:** [Golden Revision Booklet](https://vetri-tnpsc-content.vercel.app/materials/vetri_tnpsc_group4_tamil_golden_revision.pdf) (Published on Telegram channel & bot).
* **YouTube Channel:** [Vetri TNPSC: Tamil Quiz & VAO](https://www.youtube.com/@OppositeMelodies-yy8zg).
* **Instagram Profile:** [@vetri.tnpsc](https://www.instagram.com/vetri.tnpsc/).

---

## 📂 Key File Locations & Scripts

| Path | Purpose |
| :--- | :--- |
| `c:\\Moved_From_E\\Projects\\Vetri TNPSC` | Flutter Android project source code. |
| `c:\\Moved_From_E\\Projects\\vetri-tnpsc-content` | Web, API, and content synchronization repository. |
| `content.json` | Master question bank ({stats['total']} questions) auto-polled by mobile app & webapp. |
| `api/telegram.js` | 24/7 serverless webhook for `@VetriTNPSCQuizBot` on Vercel. |
| `materials/vetri_tnpsc_group4_tamil_golden_revision.pdf` | High-value 603 KB Tamil revision lead magnet. |
| `scripts/self_updater.py` | Master self-updating engine (runs on start to self-heal & self-sync). |
| `scripts/generate_quiz_short.py` | Batch generator for 1080x1920 (9:16) YouTube Shorts & Instagram Reels. |
| `scripts/post_daily_quiz.py` | Automated Telegram quiz poll dispatcher. |
| `scripts/posted_quiz_ids.json` | Live tracker of published question IDs. |
| `scripts/youtube_growth_engine.py` | Daily YouTube comment seeding automation. |
| `google_play_production_application_guide.md` | Full 20-question production access dossier for Day 14. |
| `.agent/skills/vetri-tnpsc-growth-engine/SKILL.md` | Persistent Antigravity skill loaded automatically on new sessions. |

---

## ⚡ Active Schedules & Automations
1. **Morning Telegram Quiz:** Runs daily at 07:55 AM IST (`25 2 * * *`).
2. **Evening Telegram Quiz:** Runs daily at 08:25 PM IST (`55 14 * * *`).
3. **Auto-Merge CI/CD:** Auto-merges verified PRs at 07:45 AM, 11:55 AM, and 07:50 PM IST.
4. **Self-Updating Routine:** `scripts/self_updater.py` ensures 100% synchronized state.

---

## 🎯 Active Strategic Objectives
1. **Maintain 15 Testers:** Keep daily test engagement active until target Day 14 (~Nov 15-18).
2. **Daily Content Syndication:** Post daily YouTube Shorts, Instagram Reels, and YouTube coaching comments.
3. **Day 14 Production Unlock:** When Day 14 arrives, copy answers from `google_play_production_application_guide.md` and submit.
"""
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("✅ PROJECT_MEMORY.md updated successfully.")


def update_skill(day, remaining, stats):
    content = f"""---
name: vetri-tnpsc-growth-engine
description: >
  Autonomous daily content syndication, Telegram quiz publishing, Play Store ASO monitoring,
  social media (YouTube & Instagram) automation, and organic student growth engine for the Vetri TNPSC ecosystem.
---

# Vetri TNPSC Growth & Automation Engine (Master Project Skill)

This skill serves as the single source of truth for the **Vetri TNPSC** ecosystem across Google Play, Telegram, Web, YouTube, and Instagram.

---

## 🏛️ 1. Complete Ecosystem Directory & Assets

| Component | Identifier / URL | Current Status & Details |
| :--- | :--- | :--- |
| **Mobile App (Flutter)** | `c:\\Moved_From_E\\Projects\\Vetri TNPSC` (`com.vetritnpsc.app`) | In **Closed Testing (Day {day} of {TESTING_TOTAL_DAYS})**. 15 active human testers. |
| **Play Console** | App ID: `4974456653551017111` / Dev: `5665733336363361118` | Store listing metadata approved. Target Day 14: Nov 15–18, 2026. |
| **Production Dossier** | `google_play_production_application_guide.md` | Full 20-question copy-paste answers ready for Day 14 application. |
| **Web App & API** | `https://vetri-tnpsc-content.vercel.app` | Vercel production hosting. Interactive 5-question mock test & viral rank scorecard. |
| **Content Repository** | `c:\\Moved_From_E\\Projects\\vetri-tnpsc-content` | GitHub: `maniraja5599/vetri-tnpsc-content` (branch: `main`). |
| **Golden Revision PDF**| `https://vetri-tnpsc-content.vercel.app/materials/vetri_tnpsc_group4_tamil_golden_revision.pdf` | High-value lead magnet with clickable Telegram hyperlinks. |
| **Telegram Channel** | `https://t.me/VetriTNPSCApp` (`@VetriTNPSCApp`) | 86+ members. Twice-daily automated quiz polls + PDF announcements. |
| **Telegram Bot** | `@VetriTNPSCQuizBot` (Token in Vercel & GitHub Secrets) | Webhook: `/api/telegram`. Force-join gate, `/quiz`, `/tamil`, `/ca`, `/pdf`, `/invite`. |
| **YouTube Channel** | `https://www.youtube.com/@OppositeMelodies-yy8zg` | Name: `Vetri TNPSC: Tamil Quiz & VAO`. |
| **Instagram Profile**| `https://www.instagram.com/vetri.tnpsc/` | Handle: `@vetri.tnpsc`. |
| **AdMob Account** | Pub ID: `pub-6785588120865456` | Integrated in Flutter app (`google_mobile_ads`). |

---

## ⚡ 2. Active Cloud Automations & Schedules

### A. Twice-Daily Telegram Quiz Polls
* **Workflow**: `.github/workflows/daily-telegram-quiz.yml`
* **Timing**:
  * Morning Shift: **07:55 AM IST** (`25 2 * * *`)
  * Evening Shift: **08:25 PM IST** (`55 14 * * *`)
* **Action**: Automatically takes unposted questions from `content.json`, publishes them as native Quiz Polls to `@VetriTNPSCApp`, appends 1-Tap Viral Share buttons, and commits tracker state.

### B. Telegram Bot Serverless Webhook (`api/telegram.js`)
* **Endpoint**: `https://vetri-tnpsc-content.vercel.app/api/telegram`
* **Features**:
  * **Force-Join Gate**: Blocks `/pdf` downloads until the user joins `@VetriTNPSCApp`.
  * **Referral Engine (`/invite`)**: Generates referral link and notifies inviter in real-time.
  * **On-Demand Quizzes**: Responds to `/quiz`, `/tamil`, `/ca` instantly.

### C. Automated YouTube Shorts / Instagram Reels Generator
* **Script**: `scripts/generate_quiz_short.py`
* **Output**: Generates crisp 1080x1920 (9:16) vertical videos using Chrome headless and ffmpeg.

### D. Daily YouTube Comment Seeding Engine
* **Script**: `scripts/youtube_growth_engine.py`
* **Schedule**: Target morning educational video uploads (09:00 AM – 10:00 AM IST).

### E. Self-Updating Master Engine
* **Script**: `scripts/self_updater.py`
* **Rule**: Antigravity automatically runs this script or invokes self-updating logic at the beginning of each interaction to ensure dynamic Day calculation, memory sync, and buffer preservation.

---

## 📅 3. Closed Testing 14-Day Timeline

* **Current Status**: **Day {day} of {TESTING_TOTAL_DAYS}** ({remaining} days remaining).
* **Testers**: 15 opted-in testers active in Google Play Console.
* **Target Completion Date**: **November 15–18, 2026** (Day 14).
* **Launch Action**: When "Apply for production" unlocks, copy answers directly from:
  `google_play_production_application_guide.md` and submit.
"""
    with open(SKILL_FILE, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("✅ .agent/skills/vetri-tnpsc-growth-engine/SKILL.md updated successfully.")


def main():
    print("=== Vetri TNPSC Autonomous Self-Updater ===")
    day, remaining = get_testing_day()
    stats = get_content_stats()
    shorts_count = get_shorts_count()

    print(f"📍 Testing Status: Day {day} of {TESTING_TOTAL_DAYS} ({remaining} days remaining)")
    print(f"📚 Question Bank: {stats['total']} total, {stats['posted']} posted, {stats['unposted']} in reserve")
    print(f"🎬 Video Shorts: {shorts_count} MP4 videos in shorts/")

    update_project_memory(day, remaining, stats, shorts_count)
    update_skill(day, remaining, stats)
    print("🚀 Self-updating routine completed successfully.")


if __name__ == "__main__":
    main()
