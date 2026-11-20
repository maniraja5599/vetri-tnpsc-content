# Vetri TNPSC Ecosystem - Project Memory & Handoff Summary
**Last Self-Updated:** November 20, 2026 (07:08 PM IST) · **Testing Status:** 🚀 100% LIVE ON GOOGLE PLAY STORE WORLDWIDE (Public Production Launch!)

---

## 🛑 MANDATORY CORE RULES: ANTIGRAVITY_RULES.md (Strict Override)
> **CRITICAL DIRECTIVE:** Before executing any growth or social-media task, you MUST read and follow [ANTIGRAVITY_RULES.md](file:///c:/Moved_From_E/Projects/vetri-tnpsc-content/ANTIGRAVITY_RULES.md). It strictly overrides this document, `DAILY_OPERATIONS_LOG.md`, and the `vetri-tnpsc-growth-engine` skill.
>
> 1. **Who Posts What:**
>    - **Instagram Feed Carousels & Reels / YouTube Shorts:** Owned & scheduled by Metricool (via Claude Code) from `posts/` (Nov 21 – Dec 20, 2026) and `shorts/`. Do NOT post by hand. Always check the Metricool planner first.
>    - **Telegram Polls:** Managed exclusively by GitHub Actions (`daily-telegram-quiz.yml`). Do not post extra manual polls.
>    - **Current Affairs:** Managed via PR + verify + auto-merge pipeline. Never edit `content.json` directly.
>    - **Play Store / AdMob / Console Settings:** Mani (Owner) only. Read-only.
> 2. **Allowed:**
>    - Reply politely to comments and DMs on our own channels (Tamil/Tanglish).
>    - Generate assets on-demand when requested (`scripts/make_daily_posts.py`, `scripts/generate_quiz_short.py`) into `posts/` and `shorts/` without self-posting.
>    - Log real, unhyped numbers into `DAILY_OPERATIONS_LOG.md`.
>    - Neutral review prompts ("Vetri TNPSC app பயனுள்ளதாக இருந்தால் Play Store-ல் உங்கள் review-ஐ எழுதுங்கள்").
> 3. **Strictly Prohibited (Never Do These):**
>    - ❌ NO promotional comments on other people's YouTube videos or Instagram posts (`scripts/youtube_growth_engine.py` permanently stopped).
>    - ❌ NEVER ask for "5-star" ratings or trade incentives for reviews.
>    - ❌ NO bots, fake accounts, purchased followers, or spam/mass DMs.
>    - ❌ NEVER post Vetri TNPSC content to `@anjaneyaborewells` or any other brand.
>    - ❌ NO overclaiming ("1000+ questions", "official TNPSC app"). Keep standard non-affiliation disclaimer.
>    - ❌ NEVER commit secrets (.env, tokens, keystore).
>    - ❌ NEVER spend money or change account settings without explicit owner consent.
> 4. **When in doubt:** Stop and ask Mani in one short Tanglish message.

---

## 🚀 Quick Executive Status
* **Ecosystem:** Vetri TNPSC: Tamil Quiz & VAO (`com.vetritnpsc.app`)
* **Google Play Closed Testing:** **🚀 100% LIVE ON GOOGLE PLAY STORE WORLDWIDE (Public Production Launch!)** (15 active human testers, metadata fully approved).
* **Master Question Bank:** **123 Total Questions** (91 posted, 32 unposted in reserve: 21 Tamil + 11 CA).
* **Generated Video Shorts (1080x1920 9:16):** **10 Video Shorts ready** in `shorts/`.
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
| `c:\Moved_From_E\Projects\Vetri TNPSC` | Flutter Android project source code. |
| `c:\Moved_From_E\Projects\vetri-tnpsc-content` | Web, API, and content synchronization repository. |
| `content.json` | Master question bank (123 questions) auto-polled by mobile app & webapp. |
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
1. **Maintain Active Engagement During Review:** Keep twice-daily Telegram quizzes and user tests flowing while Google evaluates the application (2-7 days).
2. **Trader Status Declaration:** Complete the EU DSA Non-Trader declaration in Google Play Console.
3. **Daily Content Syndication:** Post daily YouTube Shorts, Instagram Reels, and engage via comments.
4. **Instant Production Promotion:** As soon as Google review approves access, promote the Closed Testing release to Production Live!
