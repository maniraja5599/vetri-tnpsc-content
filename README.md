# vetri-tnpsc-content

[![Get it on Google Play](https://img.shields.io/badge/Google_Play-Vetri_TNPSC-green?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.vetritnpsc.app)
[![Web App](https://img.shields.io/badge/Web_App-Live-blue)](https://vetri-tnpsc-content.vercel.app/)
[![Telegram Channel](https://img.shields.io/badge/Telegram-@VetriTNPSCApp-2CA5E0?logo=telegram&logoColor=white)](https://t.me/VetriTNPSCApp)

Content for the **Vetri TNPSC: Tamil Quiz & VAO** Android app ([Google Play Store](https://play.google.com/store/apps/details?id=com.vetritnpsc.app)). The app downloads `content.json` from this repo, so every change here reaches users without a Play Store update.

| File | Purpose |
|---|---|
| `content.json` | Questions, current affairs, syllabus, exam date, announcements (generated: do not edit by hand) |
| `privacy-policy.html` | Privacy policy for the Play Store listing |
| `app-ads.txt` | AdMob seller verification |
| `index.html` | Small website for the app |

Edit content in the app project's `content/` folder, then run `tools/publish_content.ps1` there.
