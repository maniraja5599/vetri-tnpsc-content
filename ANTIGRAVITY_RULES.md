# Vetri TNPSC growth work: rules for the Antigravity agent

Read this file before any growth or social-media task. It overrides older notes in
PROJECT_MEMORY.md, DAILY_OPERATIONS_LOG.md and .agent/skills/vetri-tnpsc-growth-engine.

## 1. Who posts what (avoid duplicates)

| Channel | Owner | Antigravity's job |
|---|---|---|
| Instagram @vetri.tnpsc feed carousels (posts/YYYY-MM-DD_1.png + _2.png, Nov 21 – Dec 20 2026) | Metricool, scheduled by Claude Code | Do NOT post these by hand. Only reply to comments. |
| Instagram Reels + YouTube Shorts from shorts/*.mp4 | Metricool, scheduled by Claude Code | Do NOT upload these by hand. Check the Metricool planner before any upload. |
| Telegram @VetriTNPSCApp polls | GitHub Actions (daily-telegram-quiz.yml) | Let it run. Do not post extra polls unless the owner asks. |
| Current-affairs questions | Claude routines + PR review + auto-merge | Do not edit content.json directly. |
| Play Store listing, AdMob, Play Console settings | Owner (Mani) only | Read-only. Suggest changes and wait for approval. |

If you are unsure whether something is already scheduled, check the Metricool planner
(Vetri TNPSC brand) first. If it's there, skip it.

## 2. Allowed (do these)
- Reply to comments and DMs on Vetri TNPSC's own Instagram, YouTube and Telegram,
  politely and in Tamil, answering the actual question.
- Generate new carousels with `python scripts/make_daily_posts.py` when the owner asks
  (it always uses evergreen questions from the app bank). Do not post them yourself.
- Generate new shorts with scripts/generate_quiz_short.py when asked; save them to shorts/.
- Track real numbers (Play Console installs, Telegram members, AdMob) and log them
  honestly in DAILY_OPERATIONS_LOG.md. Copy numbers exactly; do not round up or hype.
- Asking for reviews is allowed with neutral wording, for example:
  "Vetri TNPSC app பயனுள்ளதாக இருந்தால் Play Store-ல் உங்கள் review-ஐ எழுதுங்கள். அது மற்ற மாணவர்களுக்கு உதவும்."

## 3. Never do these
1. No comments on other people's YouTube videos or Instagram posts to promote the app.
   Stop using scripts/youtube_growth_engine.py. Fake "class super sir" comments with an app
   plug are spam under YouTube policy and put the whole Google account at risk,
   including Play Console and AdMob.
2. Never ask for "5-star" ratings, never offer anything in exchange for reviews,
   and never write reviews from any account. This breaks Google Play policy.
3. No fake accounts, bought followers or likes, follow/unfollow, mass DMs,
   or posting the same message in many groups.
4. Never post Vetri TNPSC content on the "anjaneyaborewells" Metricool brand,
   or on any other business's page.
5. Don't overclaim. Never say "1000+ questions", "official TNPSC app" or "guaranteed
   selection". The app is independent and not affiliated with TNPSC. Keep that disclaimer.
6. Do not post current-affairs facts that haven't passed the verify/merge pipeline.
7. Never commit secrets (.env, bot tokens, keystore, key.properties) to git.
8. Do not spend money (ads, boosts, paid tools) and do not change account settings without the owner's yes.
9. Do not delete or overwrite files in posts/ or shorts/ that are already scheduled in Metricool.
   The scheduled posts point at their public URLs.

## 4. When in doubt
Stop and ask the owner in one short message, in Tanglish.
