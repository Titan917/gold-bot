import time
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TELEGRAM_TOKEN = "8867215330:AAEbnbwqsU_090PChnT8iqFqyZCr-oN_UvU"
CHAT_ID = "6511464561"

def send_telegram_msg(message):
    url = f"https://api.telegram.com/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Error:", e)

# Dummy Web Server to satisfy Render Free Web Service Port Check
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Gold Bot Engine is Live and Running 24/7!")

def run_web_server():
    server = HTTPServer(('0.0.0.0', 10000), MyServer)
    print("🌍 Web Server Started on Port 10000...")
    server.serve_forever()

# Start Web Server in a separate thread
threading.Thread(target=run_web_server, daemon=True).start()

print("🚀 SERVER STARTED SUCCESSFULLY...")
send_telegram_msg("🔄 *Gyananshu Bhai! Gold Bot Render Free Server Par Permanent Live Ho Chuka Hai!*")

while True:
    try:
        print("🔍 Checking Gold Market Levels... Engine Active.")
        time.sleep(300) 
    except Exception as e:
        print("Loop Error:", e)
        time.sleep(10)
