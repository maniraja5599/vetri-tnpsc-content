# vetri-tnpsc-content

Content for the Vetri TNPSC app. The app downloads `content.json` from this repo, so every change here reaches users without a Play Store update.

| File | Purpose |
|---|---|
| `content.json` | Questions, current affairs, syllabus, exam date, announcements (generated: do not edit by hand) |
| `privacy-policy.html` | Privacy policy for the Play Store listing |
| `app-ads.txt` | AdMob seller verification |
| `index.html` | Small website for the app |

Edit content in the app project's `content/` folder, then run `tools/publish_content.ps1` there.
