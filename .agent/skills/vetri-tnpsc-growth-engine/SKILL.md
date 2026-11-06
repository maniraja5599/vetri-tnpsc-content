---
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
| **Mobile App (Flutter)** | `c:\Moved_From_E\Projects\Vetri TNPSC` (`com.vetritnpsc.app`) | In **Closed Testing (Day 5 of 14)**. 15 active human testers. |
| **Play Console** | App ID: `4974456653551017111` / Dev: `5665733336363361118` | Store listing metadata approved. Target Day 14: Nov 15–18, 2026. |
| **Production Dossier** | `google_play_production_application_guide.md` | Full 20-question copy-paste answers ready for Day 14 application. |
| **Web App & API** | `https://vetri-tnpsc-content.vercel.app` | Vercel production hosting. Interactive 5-question mock test & viral rank scorecard. |
| **Content Repository** | `c:\Moved_From_E\Projects\vetri-tnpsc-content` | GitHub: `maniraja5599/vetri-tnpsc-content` (branch: `main`). |
| **Golden Revision PDF**| `https://vetri-tnpsc-content.vercel.app/materials/vetri_tnpsc_group4_tamil_golden_revision.pdf` | High-value lead magnet with clickable Telegram hyperlinks. |
| **Telegram Channel** | `https://t.me/VetriTNPSCApp` (`@VetriTNPSCApp`) | 86+ members. Twice-daily automated quiz polls + PDF announcements. |
| **Telegram Bot** | `@VetriTNPSCQuizBot` (Token in Vercel & GitHub Secrets) | Webhook: `/api/telegram`. Force-join gate, `/quiz`, `/tamil`, `/ca`, `/pdf`, `/invite`. |
| **YouTube Channel** | `https://www.youtube.com/@OppositeMelodies-yy8zg` | Name: `Vetri TNPSC: Tamil Quiz & VAO`. Live Short: `https://www.youtube.com/shorts/vwJTW-JtXyo`. |
| **Instagram Profile**| `https://www.instagram.com/vetri.tnpsc/` | Handle: `@vetri.tnpsc`. Live Reel: `https://www.instagram.com/reel/DfXlTSszmvE/`. |
| **AdMob Account** | Pub ID: `pub-6785588120865456` | Integrated in Flutter app (`google_mobile_ads`). Firebase linking is optional/not required. |

---

## ⚡ 2. Active Cloud Automations & Schedules

### A. Twice-Daily Telegram Quiz Polls
* **Workflow**: `.github/workflows/daily-telegram-quiz.yml`
* **Timing**:
  * Morning Shift: **08:00 AM IST** (`30 2 * * *`)
  * Evening Shift: **08:30 PM IST** (`0 15 * * *`)
* **Action**: Automatically takes unposted questions from `content.json`, publishes them as native Quiz Polls to `@VetriTNPSCApp`, appends 1-Tap Viral Share buttons, and commits tracker state.

### B. Telegram Bot Serverless Webhook (`api/telegram.js`)
* **Endpoint**: `https://vetri-tnpsc-content.vercel.app/api/telegram`
* **Features**:
  * **Force-Join Gate**: Blocks `/pdf` downloads until the user joins `@VetriTNPSCApp`.
  * **Referral Engine (`/invite`)**: Generates `t.me/VetriTNPSCQuizBot?start=ref_<USER_ID>` and notifies the referrer in real-time when a friend joins.
  * **On-Demand Quizzes**: Responds to `/quiz`, `/tamil`, `/ca` instantly.

### C. Automated YouTube Shorts / Instagram Reels Generator
* **Script**: `scripts/generate_quiz_short.py`
* **Output**: Generates crisp 1080x1920 (9:16) vertical videos using Chrome headless and ffmpeg.
* **Commands**:
  * Generate 1 short: `python scripts/generate_quiz_short.py`
  * Batch generate 5 shorts: `python scripts/generate_quiz_short.py --count 5 --start 0`

### D. Daily YouTube Comment Seeding Engine
* **Script**: `scripts/youtube_growth_engine.py`
* **Schedule**: Scheduled daily at **09:30 AM IST** (`30 9 * * *`).
* **Action**: Connects to Chrome, finds fresh morning TNPSC educational videos, and posts natural Tamil recommendation comments pointing students to `t.me/VetriTNPSCApp`.

---

## 📅 3. Closed Testing 14-Day Timeline

* **Current Status**: **Day 5 of 14** (November 6, 2026).
* **Testers**: 15 opted-in testers active in Google Play Console.
* **Target Completion Date**: **November 15–18, 2026** (Day 14).
* **Launch Action**: When "Apply for production" unlocks, copy answers directly from:
  `google_play_production_application_guide.md` and submit.
