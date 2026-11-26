# Vetri TNPSC growth work: rules for the Antigravity agent

Read this file before any growth or social-media task. It overrides older notes in
PROJECT_MEMORY.md, DAILY_OPERATIONS_LOG.md and .agent/skills/vetri-tnpsc-growth-engine.

## 1. Who posts what (avoid duplicates)

| Channel | Owner | Antigravity's job |
|---|---|---|
| Instagram @vetri.tnpsc feed carousels (posts/YYYY-MM-DD_1.png + _2.png, Nov 21 – Dec 20 2026) | Antigravity, daily task (section 5) | Post exactly one carousel per day; record it in posts/posted_social.json. |
| Instagram Reels + YouTube Shorts from shorts/*.mp4 | Antigravity, daily task (section 5) | Post one unposted short per day; record it in posts/posted_social.json. |
| Telegram @VetriTNPSCApp polls | GitHub Actions (daily-telegram-quiz.yml) | Let it run. Do not post extra polls unless the owner asks. |
| Current-affairs questions | Claude routines + PR review + auto-merge | Do not edit content.json directly. |
| Play Store listing, AdMob, Play Console settings | Owner (Mani) only | Read-only. Suggest changes and wait for approval. |

Before posting anything, check posts/posted_social.json and the live profile.
If it's already posted, skip it.

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
4. Post only as @vetri.tnpsc on Instagram and on the Vetri TNPSC YouTube channel.
   Never on "anjaneyaborewells", FiFTO or any other business's page or channel.
   Check the account name before every post.
5. Don't overclaim. Never say "1000+ questions", "official TNPSC app" or "guaranteed
   selection". The app is independent and not affiliated with TNPSC. Keep that disclaimer.
6. Do not post current-affairs facts that haven't passed the verify/merge pipeline.
7. Never commit secrets (.env, bot tokens, keystore, key.properties) to git.
8. Do not spend money (ads, boosts, paid tools) and do not change account settings without the owner's yes.
9. Do not regenerate or overwrite files in posts/ for dates that are already posted.
10. Never post more than the daily quota below. No bursts and no "catch-up" posting of
    missed days. A missed day is simply skipped.

## 4. When in doubt
Stop and ask the owner in one short message, in Tanglish.

## 5. Daily posting task (run once a day, around 7:00 PM IST)
Use the real Chrome browser where the owner is already logged in. Never type passwords.
If a login, CAPTCHA, 2-step prompt or "suspicious activity" warning appears, STOP and tell the owner.

1. Today = current date in IST (YYYY-MM-DD). Read posts/posts.json and posts/posted_social.json.
2. Instagram carousel:
   - Find the entry in posts.json whose "date" == today. If none exists, or posted_social.json
     already has today under "instagram_carousel", skip this step.
   - On instagram.com, logged in as @vetri.tnpsc (check the username first; if it is any
     other account, STOP): create a post with the two images in order (_1 then _2),
     4:5 crop, and the entry's "caption" pasted exactly.
   - After it is live, append {"date", "question_id", "url"} to "instagram_carousel".
3. Short (one per day):
   - Pick the first file in shorts/ (sorted by name) that is not in posted_social.json
     "shorts". Skip tnpsc_quiz_short_02.mp4 (already on YouTube).
   - YouTube Studio (Vetri TNPSC channel, check the channel name first): upload as a Short,
     not made for kids, title "TNPSC Group 4 பொதுத்தமிழ் வினாடி வினா #shorts #tnpsc",
     description with the Play Store link
     https://play.google.com/store/apps/details?id=com.vetritnpsc.app
   - Instagram: share the same file as a Reel on @vetri.tnpsc with a short caption plus
     "Vetri TNPSC app – link bio-வில்" and the hashtags from posts.json.
   - Append {"file", "date", "youtube_url", "instagram_url"} to "shorts".
     When all shorts are used, skip this step and tell the owner new shorts are needed.
4. Reply to new comments on today's and yesterday's posts (rules in section 2).
5. Add one honest line to DAILY_OPERATIONS_LOG.md: what was posted, plus the links.
6. Commit only posts/posted_social.json and DAILY_OPERATIONS_LOG.md with the message
   "chore: daily social post YYYY-MM-DD". Do not push other files.
7. After Dec 20 2026 (posts.json runs out), ask the owner before generating the next 30 days:
   `python scripts/make_daily_posts.py --days 30 --start <next date> --first-number 31 --seed <new number>`
