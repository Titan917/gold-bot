import time
import requests

TELEGRAM_TOKEN = "8867215330:AAEbnbwqsU_090PChnT8iqFqyZCr-oN_UvU"
CHAT_ID = "6511464561"

def send_telegram_msg(message):
    url = f"https://api.telegram.com/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Error:", e)

print("🚀 SERVER STARTED SUCCESSFULLY...")
send_telegram_msg("🔄 *Gyananshu Bhai! Gold Bot Render Server Par 24/7 Live Ho Chuka Hai!*")

while True:
    try:
        print("🔍 Checking Gold Market Levels... Engine Active.")
        time.sleep(300) 
    except Exception as e:
        print("Loop Error:", e)
        time.sleep(10)
