import time
import requests
import telegram
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def send_signal(signal, confidence):
    message = f"📊 Signal: {signal}\n✅ Confidence: {confidence}%"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def analyze_market():
    # Tusaale ahaan signal
    return "BUY", 78.5

while True:
    try:
        signal, confidence = analyze_market()
        send_signal(signal, confidence)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(60)
