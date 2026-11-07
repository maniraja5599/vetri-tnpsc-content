# Vetri TNPSC Ecosystem - Project Memory & Handoff Summary
**Last Updated:** November 7, 2026 (11:15 AM IST) · **Testing Status:** Day 6 of 14

---

## 🚀 Quick Executive Status
* **Ecosystem:** Vetri TNPSC: Tamil Quiz & VAO (`com.vetritnpsc.app`)
* **Google Play Closed Testing:** **Day 6 of 14** (15 active human testers, metadata fully approved).
* **Master Question Bank:** **56 Total Questions** (18 posted, 38 unposted, across Samacheer Kalvi Tamil and Current Affairs).
* **Web App:** [https://vetri-tnpsc-content.vercel.app](https://vetri-tnpsc-content.vercel.app) (Live 5-Q Test, Gamified Scorecard, WhatsApp Status Share).
* **Telegram Channel:** [@VetriTNPSCApp](https://t.me/VetriTNPSCApp) (86+ subscribers, automated morning 8 AM & evening 8:30 PM polls).
* **Telegram Bot:** `@VetriTNPSCQuizBot` (Vercel serverless webhook, Force-Join PDF Funnel, `/invite` Referral Engine, `/tamil` and `/ca` question filters).
* **Lead Magnet PDF:** [Golden Revision Booklet](https://vetri-tnpsc-content.vercel.app/materials/vetri_tnpsc_group4_tamil_golden_revision.pdf) (Published on Telegram channel & bot).
* **YouTube Channel:** [Vetri TNPSC: Tamil Quiz & VAO](https://www.youtube.com/@OppositeMelodies-yy8zg) (Live Short: `/shorts/vwJTW-JtXyo`).
* **Instagram Profile:** [@vetri.tnpsc](https://www.instagram.com/vetri.tnpsc/) (Live Reel: `/reel/DfXlTSszmvE/`).
* **Generated Video Shorts (1080x1920 9:16):**
  * `shorts/tnpsc_quiz_short_54.mp4` (Nov 7 Sports CA: Asian Champions Trophy Hockey 4-1 Victory vs Japan)
  * `shorts/tnpsc_quiz_short_41.mp4` (General Tamil: "சொல்லின் செல்வர்" ரா. பி. சேதுப்பிள்ளை)
  * `shorts/tnpsc_quiz_short_04.mp4` (Current Affairs: DA hike)
  * `shorts/tnpsc_quiz_short_05.mp4` (Current Affairs: PM Gram Swaraj)

---

## 📂 Key File Locations & Scripts

| Path | Purpose |
| :--- | :--- |
| `c:\Moved_From_E\Projects\Vetri TNPSC` | Flutter Android project source code. |
| `c:\Moved_From_E\Projects\vetri-tnpsc-content` | Web, API, and content synchronization repository. |
| `content.json` | Master question bank (56 questions) auto-polled by mobile app & webapp. |
| `api/telegram.js` | 24/7 serverless webhook for `@VetriTNPSCQuizBot` on Vercel. |
| `materials/vetri_tnpsc_group4_tamil_golden_revision.pdf` | High-value 589 KB Tamil revision lead magnet. |
| `scripts/generate_quiz_short.py` | Batch generator for 1080x1920 (9:16) YouTube Shorts & Instagram Reels. |
| `scripts/post_daily_quiz.py` | Automated Telegram quiz poll dispatcher (with option safety & sleep throttling). |
| `scripts/posted_quiz_ids.json` | Live tracker of published question IDs. |
| `scripts/youtube_growth_engine.py` | Daily YouTube comment seeding automation. |
| `google_play_production_application_guide.md` | Full 20-question production access dossier for Day 14. |
| `.agent/skills/vetri-tnpsc-growth-engine/SKILL.md` | Persistent Antigravity skill loaded automatically on new sessions. |

---

## ⚡ Automated CI/CD & Auto-Merge + Telegram Dispatch Flow
1. **Pull Request Trigger & Auto-Merge (`.github/workflows/auto-merge.yml`):**
   * Daily CA branch `ca-YYYY-MM-DD` is created.
   * Auto-merge triggers on: PR open/label/sync, comment `VERIFIED`, and cron (07:30 AM, 12:00 PM, 08:00 PM IST).
   * Validates via `.github/check.js` (valid JSON, increased version, non-empty fields, exactly 4 unique options, 0-3 answer index) and `.github/approved.js`.
   * Merges automatically via squash and deletes the branch.
2. **Instant Push-to-Telegram Dispatch (`.github/workflows/daily-telegram-quiz.yml`):**
   * Triggered automatically on every push/merge to `main` modifying `content.json`.
   * Also triggered on schedule: Morning 08:00 AM IST & Evening 08:30 PM IST.
   * Selects newly merged unposted questions, sends native quiz polls to `@VetriTNPSCApp` with 1-Tap Viral Share buttons.
   * Commits `scripts/posted_quiz_ids.json` with `[skip ci]` and rebase concurrency safety.

---

## 🎯 Active Strategic Objectives
1. **Daily Video Upload:** Upload `shorts/tnpsc_quiz_short_54.mp4` (Asian Champions Trophy Hockey) to YouTube Shorts & Instagram Reels.
2. **Comment Seeding:** Post morning comments on fresh TNPSC educator uploads.
3. **Closed Testing Day 14 Milestones:** Day 6 of 14 active. 8 days remaining until ~Nov 15-18 production submission.
