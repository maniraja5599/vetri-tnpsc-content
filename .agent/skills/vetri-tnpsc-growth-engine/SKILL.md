---
name: vetri-tnpsc-growth-engine
description: >
  Autonomous daily content syndication, Telegram quiz publishing, Play Store ASO monitoring,
  and organic student marketing automation engine for the Vetri TNPSC app ecosystem.
---

# Vetri TNPSC Growth & Automation Engine

This skill encapsulates the end-to-end autonomous distribution, content pipeline, community marketing, and app store growth workflows for **Vetri TNPSC: Tamil Quiz** (`com.vetritnpsc.app`).

---

## 🏛️ 1. Ecosystem Architecture

| Component | Identifier / Location | Purpose |
| :--- | :--- | :--- |
| **Mobile App** | `c:\Moved_From_E\Projects\Vetri TNPSC` (`com.vetritnpsc.app`) | Flutter quiz app (Group 4, 2, VAO). Bundled Samacheer Tamil + remote dynamic sync. |
| **Content & Web Repo** | `c:\Moved_From_E\Projects\vetri-tnpsc-content` (`maniraja5599/vetri-tnpsc-content`) | Source of truth for `content.json`, `app-ads.txt`, and landing page assets. |
| **Live Landing Page** | `https://vetri-tnpsc-content.vercel.app` | Vercel production hosting, Google Play redirect, Telegram CTA, rich OpenGraph cards. |
| **Telegram Channel** | `https://t.me/VetriTNPSCApp` (`@VetriTNPSCApp`) | Primary community channel for daily polls, exam alerts, and student engagement. |
| **Telegram Bot** | `@VetriTNPSCQuizBot` (Managed via GitHub Secrets `TELEGRAM_BOT_TOKEN`) | Cloud bot with admin rights to post native Quiz Polls and promo announcements. |
| **Global Directory** | TGStat (`https://tgstat.ru/en/channel/@VetriTNPSCApp`) | Search index and analytics engine for organic discoverability. |

---

## ⚡ 2. Autonomous Cloud Pipelines (100% Hands-Free)

### A. Daily Telegram Quiz Poster
* **Workflow**: `.github/workflows/daily-telegram-quiz.yml`
* **Trigger**: Scheduled via Cron `30 2 * * *` (Every morning at **08:00 AM IST** / 02:30 UTC).
* **Script**: `scripts/post_daily_quiz.py`
* **Action**:
  1. Pulls latest `content.json`.
  2. Identifies unposted questions from `scripts/posted_quiz_ids.json`.
  3. Dispatches 2 questions as native Telegram Quiz Polls via `sendPoll` (with correct answers & explanations).
  4. Appends promotional CTA with `https://vetri-tnpsc-content.vercel.app`.
  5. Commits updated tracking state back to Git repository.

### B. Daily Content Pipeline
* **Workflow**: `.github/workflows/auto-merge.yml`
* **Action**: Merges daily AI-generated current affairs and question PRs into `main`.
* **Client App Sync**: The mobile app's `ContentService` auto-polls `content.json` every 3 hours or on app launch without needing Play Store app updates.

### C. Continuous Deployment (Vercel)
* **Action**: Any commit pushed to `origin/main` automatically rebuilds and deploys `index.html`, `app-ads.txt`, and rich social preview graphics (`og-image.png`) in < 20 seconds.

---

## 🛠️ 3. Operational & Diagnostic Commands

### Run Telegram Quiz Immediately (Manual Trigger)
```bash
python c:\Moved_From_E\Projects\vetri-tnpsc-content\scripts\post_daily_quiz.py
```

### Inspect Telegram Bot & Channel Connection
```python
import urllib.request, json
token = os.environ.get("TELEGRAM_BOT_TOKEN")
url = f"https://api.telegram.org/bot{token}/getChat?chat_id=@VetriTNPSCApp"
with urllib.request.urlopen(url) as r:
    print(json.loads(r.read().decode('utf-8')))
```

### Verify Live Remote Content JSON
```bash
curl -I https://vetri-tnpsc-content.vercel.app/content.json
```

---

## 📣 4. Community Growth & Marketing Playbook

### 1. Daily 5-Minute Morning Routine
1. At **08:00 AM**, verify today's automated Telegram quiz dropped into `@VetriTNPSCApp`.
2. Forward the quiz poll from the channel into 2–3 active TNPSC discussion groups on Telegram. (Because it is forwarded from the channel, the channel header is clickable and acts as a direct join link).
3. Post the morning WhatsApp capsule to personal and student study circles:
   ```text
   ☀️ இன்றைய TNPSC நடப்பு நிகழ்வுகள் & தமிழ் வினாடி வினா!
   👉 [t.me/VetriTNPSCApp]
   📲 இலவச செயலி: [https://vetri-tnpsc-content.vercel.app]
   ```

### 2. High-Intent Organic Channels
* **Daily YouTube Comment Engine**: Run `python scripts/youtube_growth_engine.py` to generate 3 daily, unique, spam-safe Tamil comment variations and target URLs for fresh morning TNPSC current affairs and Tamil classes.
* **Quora Strategy**: Answer high-traffic queries like *"How do I prepare for TNPSC Group 4?"* linking to the study method and app (`quora.com/How-do-I-prepare-for-tnpsc-group-4/answer/Mani-Raja-33`).
* **Facebook Groups**: Share tricky Samacheer grammar questions in groups with 100K+ members prompting users to comment their answer, with the app link in footer.
* **In-App Share Cards**: Encourage users to share their 10/10 quiz score cards to WhatsApp Status.

---

## 📋 5. Pre-Launch & Launch Day Checklist

1. **Closed Testing Track (Until ~Nov 14, 2026)**:
   - Ensure >= 12 opted-in testers maintain the app installed for 14 continuous days.
   - Fill out the 20-question "Apply for production" self-assessment in Play Console.
2. **Production Launch Day Blitz**:
   - Coordinate with the 15 closed testers to submit 5-star ratings and Tamil reviews within 24 hours.
   - Navigate to `https://admob.google.com/v2/apps/confirm` and link the live Google Play listing to finalize AdMob monetization.
