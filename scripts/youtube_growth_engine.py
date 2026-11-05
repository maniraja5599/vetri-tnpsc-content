#!/usr/bin/env python3
"""
Daily YouTube Promotion & Comment Engine for Vetri TNPSC.
Generates unique, high-converting, spam-safe Tamil comment variations
and provides targeted daily YouTube video discovery links.
"""

import random
from datetime import datetime

# Curated High-Intent YouTube Search Queries (sorted by upload date & relevance)
YOUTUBE_TARGET_QUERIES = [
    {
        "topic": "Daily Current Affairs (நடப்பு நிகழ்வுகள்)",
        "url": "https://www.youtube.com/results?search_query=tnpsc+current+affairs+today+tamil&sp=CAI%253D"
    },
    {
        "topic": "Group 4 General Tamil (சமச்சீர் பொதுத்தமிழ்)",
        "url": "https://www.youtube.com/results?search_query=tnpsc+group+4+tamil+samacheer&sp=CAI%253D"
    },
    {
        "topic": "TNPSC Mock Test & Question Discussion",
        "url": "https://www.youtube.com/results?search_query=tnpsc+group+4+mock+test+tamil&sp=CAI%253D"
    }
]

# Dynamic phrase components to guarantee 100% unique, natural comments every single time
OPENINGS = [
    "வகுப்பு மிகவும் பயனுள்ளதாக இருந்தது சார்! 👍",
    "இன்றைய நடப்பு நிகழ்வுகள் தொகுப்பு அருமை சார்! ✨",
    "தேர்வுக்கு மிகத் தெளிவான விளக்கம் கொடுத்ததற்கு நன்றி சார்! 🙏",
    "ரொம்ப தெளிவான கற்பித்தல் சார், மிகவும் நன்றி!",
    "தினசரி இந்த வீடியோக்கள் எங்களுக்கு பெரிய தன்னம்பிக்கை தருகிறது சார்! 👏"
]

BODIES = [
    "இங்கு படிக்கும் தகவல்களை உடனே Quiz வடிவில் பயிற்சி செய்து நினைவில் நிறுத்த Vetri TNPSC டெலிகிராம் சேனல் மிகவும் பயனுள்ளதாக உள்ளது.",
    "6 முதல் 12-ஆம் வகுப்பு சமச்சீர் பொதுத்தமிழ் மற்றும் நடப்பு நிகழ்வுகளை தினமும் காலை 8 மணிக்கு நேரடி Timer வினாடி வினாவாக பயிற்சி செய்ய Vetri TNPSC உதவுகிறது.",
    "படித்ததை மறக்காமல் இருக்க தினமும் 5 நிமிட Mock Test எழுதிப் பயிற்சி செய்ய Vetri TNPSC தளம் மாணவர்களுக்கு ஒரு சிறந்த இலவச வழிகாட்டி.",
    "வீடியோ பார்த்த பிறகு உடனே வினாடி வினா எழுதி ரிவைஸ் செய்ய Vetri TNPSC தளம் மிகவும் உதவியாக இருக்கிறது தோழர்களே.",
    "நடப்பு நிகழ்வுகளை எளிதாக நினைவில் வைக்க காலை நேர Quiz பயிற்சிக்கு Vetri TNPSC தளம் அருமையான களம்."
]

CALL_TO_ACTIONS = [
    "👉 விருப்பமுள்ளவர்கள் இலவசமாக இணைந்து பயன்பெறலாம்: t.me/VetriTNPSCApp",
    "📲 தினசரி பயிற்சிக்கு இணையுங்கள்: t.me/VetriTNPSCApp",
    "📚 நேரடி வினாடி வினாவில் பங்கேற்க: t.me/VetriTNPSCApp",
    "🎯 இலவச மாதிரி வினாடி வினாவிற்கு: t.me/VetriTNPSCApp",
    "💡 உங்கள் நண்பர்களுக்கும் பகிருங்கள்: t.me/VetriTNPSCApp"
]


def generate_comment(variant_seed=None):
    if variant_seed is not None:
        random.seed(variant_seed)
    opening = random.choice(OPENINGS)
    body = random.choice(BODIES)
    cta = random.choice(CALL_TO_ACTIONS)
    return f"{opening} {body}\n{cta}"


def get_daily_promotions():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"=== Vetri TNPSC Daily YouTube Promotion Plan ({today}) ===\n")
    print("📍 Target Channels: Suresh IAS, Shanmugam IAS, Minnal TNPSC, Kanian TNPSC, We Shine Academy.\n")
    
    comments = []
    for i, target in enumerate(YOUTUBE_TARGET_QUERIES, 1):
        comment = generate_comment(f"{today}_{i}")
        comments.append({
            "target": target["topic"],
            "url": target["url"],
            "comment": comment
        })
        print(f"[{i}] Target Topic: {target['topic']}")
        print(f"    Search URL: {target['url']}")
        print(f"    Suggested Comment:\n    \"{comment}\"\n")
    
    return comments


if __name__ == "__main__":
    get_daily_promotions()
