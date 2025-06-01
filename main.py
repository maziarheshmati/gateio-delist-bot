import requests
import time
import xml.etree.ElementTree as ET

rss_url = "https://www.gate.io/rss/delisted"
bot_token = "7010617587:AAE4yNYQaalvO38QuRRTndISFZkwz9jfkig"
chat_id = "7385003321"
seen_titles = []

def check_rss():
    global seen_titles
    try:
        response = requests.get(rss_url)
        root = ET.fromstring(response.content)
        for item in root.findall(".//item"):
            title = item.find("title").text
            link = item.find("link").text
            if title not in seen_titles:
                seen_titles.append(title)
                if "delist" in title.lower():
                    send_message(f"🚨 خبر جدید Delist:\n\n{title}\n{link}")
    except Exception as e:
        print("خطا:", e)

def send_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

while True:
    check_rss()
    time.sleep(600)
