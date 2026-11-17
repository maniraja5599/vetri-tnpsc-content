import urllib.request
import urllib.parse
import json
import os

token = None
with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("TELEGRAM_BOT_TOKEN="):
            token = line.strip().split("=", 1)[1].strip("\"'")

if not token:
    print("No token")
    exit(1)

new_desc = (
    "🎯 TNPSC Group 4, 2 & VAO பொதுத்தமிழ் & நடப்பு நிகழ்வுகள் தினசரி மாதிரித் தேர்வு!\n"
    "📲 Play Store-ல் Install செய்ய: https://play.google.com/store/apps/details?id=com.vetritnpsc.app\n"
    "🌐 Web Mock Test: https://vetri-tnpsc-content.vercel.app"
)

url = f"https://api.telegram.org/bot{token}/setChatDescription"
data = urllib.parse.urlencode({"chat_id": "@VetriTNPSCApp", "description": new_desc}).encode("utf-8")
try:
    res = urllib.request.urlopen(urllib.request.Request(url, data=data))
    print("Updated description successfully:", res.read().decode())
except Exception as e:
    print("Error:", e)
