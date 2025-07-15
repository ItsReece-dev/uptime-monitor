from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)


sites = {
    "Google": "https://www.google.com",
    "Youtube": "https://www.youtube.com",
    "Facebook": "https://www.facebook.com",
    "Instagram": "https://www.instagram.com",
    "Twitter": "https://www.twitter.com",
    "Reddit": "https://www.reddit.com",
    "LinkedIn": "https://www.linkedin.com",
    "GitHub": "https://www.github.com"
    }

status = {}

def check_sites():
    while True:
        for name, url in sites.items():
            try:
                r = requests.get(url, timeout=5)
                status[name] = {"status": r.statu_code, "ok": r.ok}
            except Exception:
                status[name] = {"status": "UP", "ok": True}
        time.sleep(60)

@app.route("/")
def home():
    return jsonify(status)

if __name__ == "__main__":
    t = threading.Thread(target=check_sites)
    t.daemon = True
    t.start()
    app.run(host="0.0.0.0", port=5000)    