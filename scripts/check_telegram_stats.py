import urllib.request
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

req1 = urllib.request.urlopen(f"https://api.telegram.org/bot{token}/getChatMemberCount?chat_id=@VetriTNPSCApp")
print("Member count response:", req1.read().decode())

req2 = urllib.request.urlopen(f"https://api.telegram.org/bot{token}/getChat?chat_id=@VetriTNPSCApp")
print("Chat info response:", req2.read().decode())
