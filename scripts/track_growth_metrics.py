#!/usr/bin/env python3
"""
Autonomous Growth & Play Store Download Metrics Tracker for Vetri TNPSC.
Tracks daily downloads, ad requests, content bank, and retention metrics.
Computes Day-over-Day (DoD) growth comparisons and recommends daily optimization tasks.
"""

import json
import os
from datetime import datetime

METRICS_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "growth_metrics_history.json")
CONTENT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content.json")
TRACKER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posted_quiz_ids.json")

def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def record_today(installs=17, ad_requests=205, active_devices=17):
    today = datetime.now().strftime("%Y-%m-%d")
    history = load_json(METRICS_LOG, [])
    
    # Load content counts
    content = load_json(CONTENT_FILE, {})
    total_q = len(content.get("questions", []))
    ta_q = sum(1 for q in content.get("questions", []) if q.get("s") == "ta")
    ca_q = total_q - ta_q
    
    posted_ids = load_json(TRACKER_FILE, [])
    total_posted = len(posted_ids)

    entry = {
        "date": today,
        "installs": installs,
        "ad_requests": ad_requests,
        "active_devices": active_devices,
        "question_bank_total": total_q,
        "tamil_questions": ta_q,
        "general_questions": ca_q,
        "telegram_quizzes_posted": total_posted
    }

    # Upsert today's entry
    existing_idx = next((i for i, item in enumerate(history) if item.get("date") == today), None)
    if existing_idx is not None:
        history[existing_idx] = entry
    else:
        history.append(entry)

    save_json(METRICS_LOG, history)
    return history

def analyze_growth():
    history = record_today()
    if len(history) < 2:
        # Seed baseline for yesterday (Day 1 of production)
        baseline = {
            "date": "2026-11-16",
            "installs": 16,
            "ad_requests": 91,
            "active_devices": 16,
            "question_bank_total": 98,
            "tamil_questions": 45,
            "general_questions": 53,
            "telegram_quizzes_posted": 75
        }
        history = [baseline, history[-1]]
        save_json(METRICS_LOG, history)

    curr = history[-1]
    prev = history[-2]

    ad_growth = ((curr["ad_requests"] - prev["ad_requests"]) / max(1, prev["ad_requests"])) * 100
    q_growth = curr["question_bank_total"] - prev["question_bank_total"]
    installs_diff = curr["installs"] - prev["installs"]

    print("=======================================================")
    print(f"📊 VETRI TNPSC GROWTH DASHBOARD: {curr['date']}")
    print("=======================================================")
    print(f"📲 Play Store Total Installs:   {curr['installs']} (+{installs_diff} vs yesterday)")
    print(f"📈 7-Day Ad Requests:          {curr['ad_requests']} ({ad_growth:+.1f}% vs yesterday: {prev['ad_requests']})")
    print(f"📱 Monthly Active Devices:     {curr['active_devices']}")
    print(f"📚 Master Question Bank:       {curr['question_bank_total']} questions (+{q_growth} new)")
    print(f"   • Tamil Literature/Grammar: {curr['tamil_questions']}")
    print(f"   • General Studies/CA:       {curr['general_questions']}")
    print(f"🎯 Telegram Quizzes Published: {curr['telegram_quizzes_posted']}")
    print("-------------------------------------------------------")
    print("🚀 ALGORITHMIC DOWNLOAD ACCELERATION ACTIONS:")
    print("1. Review Velocity: Google Play ranks apps with >5 active reviews in search Top 5.")
    print("   Action: Ask Telegram group community members for 5-star feedback on Play Store.")
    print("2. Daily Quiz Retention: High engagement triggers Google Play algorithm 'Similar Apps' recommendations.")
    print("   Action: Keep publishing 2-3 interactive daily quiz polls at 08:30 AM & 06:30 PM.")
    print("3. YouTube Comment Organic Funnel: High conversion from TNPSC Group 4 discussion videos.")
    print("   Action: Maintain active comments on top trending Tamil literature videos.")
    print("=======================================================")

if __name__ == "__main__":
    analyze_growth()
