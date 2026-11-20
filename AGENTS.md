# Vetri TNPSC: Agent Operating Rules & Growth Directives

Before executing any task in this workspace, all agents must read and strictly adhere to [ANTIGRAVITY_RULES.md](file:///c:/Moved_From_E/Projects/vetri-tnpsc-content/ANTIGRAVITY_RULES.md).
It takes absolute precedence over `PROJECT_MEMORY.md`, `DAILY_OPERATIONS_LOG.md`, and `.agent/skills/vetri-tnpsc-growth-engine`.

## Key Rules Summary:
1. **Posting Ownership & Channel Isolation:**
   - **Instagram `@vetri.tnpsc` Carousels & Reels / YouTube Shorts:** Exclusively owned and scheduled via Metricool (by Claude Code). Do NOT upload or post these manually. Always inspect the Metricool planner first.
   - **Telegram `@VetriTNPSCApp` Polls:** Handled exclusively by `.github/workflows/daily-telegram-quiz.yml`. Do not publish manual polls unless explicitly commanded by Mani Raja.
   - **Current Affairs Content:** Must pass through the automated PR + verification + auto-merge pipeline. Never edit `content.json` directly.
   - **Play Store & AdMob Management:** Mani Raja (Owner) only. Suggest optimizations and wait for explicit approval.

2. **Allowed Operations:**
   - Answer comments and incoming DMs on our official channels politely in Tamil/Tanglish.
   - Generate creative assets (`scripts/make_daily_posts.py`, `scripts/generate_quiz_short.py`) to `posts/` and `shorts/` when asked.
   - Record exact, unhyped metrics into `DAILY_OPERATIONS_LOG.md`.
   - Ask for app reviews using neutral phrasing (e.g., *"Vetri TNPSC app பயனுள்ளதாக இருந்தால் Play Store-ல் உங்கள் review-ஐ எழுதுங்கள்"*).

3. **Strict Banned Actions (Immediate Disqualification):**
   - ❌ Promotional commenting on third-party YouTube videos or Instagram accounts (`youtube_growth_engine.py` permanently terminated).
   - ❌ Asking for "5-star" ratings, trading rewards for reviews, or writing self-reviews.
   - ❌ Fake accounts, bot engagement, mass group forwards, or spam DMs.
   - ❌ Posting Vetri TNPSC content to `@anjaneyaborewells` or other personal/client brands.
   - ❌ Exaggerated claims ("1000+ questions", "official app").
   - ❌ Committing secrets or credentials to git.
   - ❌ Spending money or modifying account settings without Mani Raja's explicit consent.

4. **Default Decision Protocol:**
   - When in doubt, STOP immediately and ask Mani Raja in one short Tanglish message.
