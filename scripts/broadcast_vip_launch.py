import os
import json
import urllib.request
import urllib.parse

def broadcast_vip():
    token = None
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    token = line.strip().split("=", 1)[1].strip("\"'")

    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found in .env")
        return

    chat_id = "@VetriTNPSCApp"

    msg_text = (
        "👑 <b>வெற்றி TNPSC மாணவர்களுக்கு பிரத்யேக அறிமுக சலுகை!</b> 🌟\n\n"
        "TNPSC Group 4 & Group 2 தேர்வில் அதிக மதிப்பெண் பெற்று அரசுப்பணி கனவை நனவாக்க "
        "<b>VIP MEGA PASS</b> இப்போது நேரலையாகிவிட்டது! 📚✨\n\n"
        "🔥 <b>VIP பாஸ் மூலம் நீங்கள் பெறுபவை:</b>\n"
        "✅ <b>1. முழு 50-வினாக்கள் OMR மாதிரித் தேர்வுகள்:</b> நேரடி தேர்வு அனுபவம் & உடனடி மதிப்பெண்.\n"
        "✅ <b>2. 6 முதல் 12-ஆம் வகுப்பு சமச்சீர் 1,000 வினா-விடை Golden Revision PDF:</b> முழு பாடப்பகுதி சுருக்கம்.\n"
        "✅ <b>3. 2026 நடப்பு நிகழ்வுகள் & Shortcut குறிப்புகள்.</b>\n"
        "✅ <b>4. வாழ்நாள் அணுகல் (Lifetime Access) & விளம்பரமில்லா பயிற்சி.</b>\n\n"
        "💥 <b>அறிமுக சலுகை கட்டணம்:</b> வெறும் <b>₹29 மட்டும்!</b> <del>₹199</del> (85% சிறப்பு தள்ளுபடி)\n\n"
        "💳 <b>நேரடி UPI விவரங்கள்:</b>\n"
        "• UPI ID: <code>maniraja@kvb</code>\n"
        "• பெயர்: <b>Mani Raja</b>\n"
        "• தொகை: <b>₹29</b>\n\n"
        "👇 <b>கீழே உள்ள பட்டனைத் தட்டி உடனடியாக PhonePe / GPay மூலம் செலுத்தி VIP அன்லாக் செய்துகொள்ளலாம்!</b>"
    )

    upi_deep_link = "upi://pay?pa=maniraja@kvb&pn=Mani%20Raja&tn=Vetri%20TNPSC%20VIP%20Pass&am=29&cu=INR"
    webapp_url = "https://vetri-tnpsc-content.vercel.app"
    bot_vip_url = "https://t.me/VetriTNPSCQuizBot?start=vip"
    wa_confirm_url = "https://wa.me/918300030123?text=" + urllib.parse.quote("வணக்கம் Mani! நான் Vetri TNPSC VIP Pass ₹29 செலுத்திவிட்டேன். எனது UTR எண்: ")

    payload = {
        "chat_id": chat_id,
        "text": msg_text,
        "parse_mode": "HTML",
        "reply_markup": json.dumps({
            "inline_keyboard": [
                [
                    {"text": "⚡ Webapp-ல் ₹29 செலுத்தி VIP பெற (PhonePe/GPay/QR)", "url": webapp_url}
                ],
                [
                    {"text": "🤖 Telegram Bot-ல் VIP அன்லாக் செய்ய (/vip)", "url": bot_vip_url}
                ],
                [
                    {"text": "💬 கட்டணம் செலுத்திய பின் UTR அனுப்ப (WhatsApp)", "url": wa_confirm_url}
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
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            if data.get("ok"):
                print("✅ VIP Launch broadcast sent successfully to @VetriTNPSCApp! Message ID:", data["result"]["message_id"])
            else:
                print("❌ Failed to broadcast:", data)
    except Exception as e:
        print("❌ Error during broadcast:", e)

if __name__ == "__main__":
    broadcast_vip()
