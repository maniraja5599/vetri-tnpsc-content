import os
import json
import urllib.request

def pin_message():
    token = None
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("TELEGRAM_BOT_TOKEN="):
                    token = line.strip().split("=", 1)[1].strip("\"'")

    if not token:
        print("No token found")
        return

    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/pinChatMessage",
        data=json.dumps({"chat_id": "@VetriTNPSCApp", "message_id": 121, "disable_notification": False}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    try:
        res = urllib.request.urlopen(req)
        print("Pinned announcement successfully:", json.loads(res.read().decode("utf-8")))
    except Exception as e:
        print("Error pinning message:", e)

if __name__ == "__main__":
    pin_message()
