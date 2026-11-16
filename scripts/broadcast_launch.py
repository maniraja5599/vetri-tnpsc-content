import os
import json
import urllib.request
import urllib.parse

def broadcast():
    token = None
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    token = line.strip().split("=", 1)[1].strip("\"'")

    if not token:
        print("Token not found in .env")
        return

    chat_id = "@VetriTNPSCApp"

    msg_text = (
        "🎉 <b>பெருமித அறிவிப்பு: Vetri TNPSC App இப்போது Google Play Store-ல் அதிகாரப்பூர்வமாக Live!</b> 🚀\n\n"
        "அன்பான TNPSC ஆஸ்பிரண்ட்ஸ் அனைவருக்கும் வணக்கம்!\n\n"
        "நமது <b>Vetri TNPSC: Tamil Quiz & VAO</b> மொபைல் ஆப் இப்போது கூகுள் பிளே ஸ்டோரில் உலகம் முழுவதிலும் உள்ள மாணவர்கள் "
        "இலவசமாகப் பதிவிறக்கம் செய்யும் வகையில் நேரலையாகிவிட்டது! 🏆\n\n"
        "✨ <b>முக்கிய சிறப்பம்சங்கள்:</b>\n"
        "📚 6 முதல் 12-ஆம் வகுப்பு சமச்சீர் கல்வி பொதுத்தமிழ் வினா வங்கி\n"
        "🎯 தினசரி நடப்பு நிகழ்வுகள் & விரிவான பாடநூல் விளக்கக் குறிப்புகள்\n"
        "⏱️ தேர்வு போன்ற 15-வினாடி Timer & உடனடி Scorecard\n"
        "💾 ஆஃப்லைனிலும் வினாடி வினா பயிற்சி செய்யும் வசதி\n"
        "💯 100% இலவசம் (மாணவர்களுக்கான தடையற்ற சேவை)\n\n"
        "👇 <b>கீழே உள்ள பட்டனை அழுத்தி இப்போதே Play Store-ல் Install செய்துகொள்ளுங்கள்!</b>"
    )

    share_text = "🎯 TNPSC Group 4 & Group 2 பொதுத்தமிழ் மற்றும் நடப்பு நிகழ்வுகள் பயிற்சி செய்ய சிறந்த ஆப் 'Vetri TNPSC'! Play Store-ல் இலவசமாகப் பதிவிறக்க: "
    share_url = "https://t.me/share/url?" + urllib.parse.urlencode({
        "url": "https://play.google.com/store/apps/details?id=com.vetritnpsc.app",
        "text": share_text
    })

    payload = {
        "chat_id": chat_id,
        "text": msg_text,
        "parse_mode": "HTML",
        "reply_markup": json.dumps({
            "inline_keyboard": [
                [
                    {"text": "📲 Google Play Store-ல் Install செய்ய", "url": "https://play.google.com/store/apps/details?id=com.vetritnpsc.app"}
                ],
                [
                    {"text": "🌐 Browser-ல் Online Mock Test பயிற்சி செய்ய", "url": "https://vetri-tnpsc-content.vercel.app"}
                ],
                [
                    {"text": "🚀 நண்பர்களுக்குப் பகிருங்கள் (1-Tap Share)", "url": share_url}
                ]
            ]
        })
    }

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode("utf-8"))
        print(f"Broadcast success! Message ID: {data['result']['message_id']}")
    except Exception as e:
        print("Error sending telegram broadcast:", e)

if __name__ == "__main__":
    broadcast()
