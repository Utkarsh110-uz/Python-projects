"""
Gmail → Telegram Forwarder Bot
================================
Polls your Gmail inbox every 10 seconds and forwards new emails to your Telegram DM.
Includes a built-in web server so Replit stays awake via UptimeRobot.
Sends clean, short, plain-text only messages — no HTML, no images, no junk.
"""

import imaplib
import email
from email.header import decode_header
import time
import requests
import json
import os
import html
import re
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# ─────────────────────────────────────────────
#  ✏️  FILL IN YOUR CREDENTIALS BELOW
# ─────────────────────────────────────────────

TELEGRAM_BOT_TOKEN = "Bot_token" # From @BotFather
TELEGRAM_CHAT_ID   = "Chat_ID" # Your numeric chat ID

GMAIL_ADDRESS      = "Your_email" # Your Gmail address
GMAIL_APP_PASSWORD = "Gmail_app_password" # 16-char App Password

# ─────────────────────────────────────────────
#  ⚙️  SETTINGS
# ─────────────────────────────────────────────

CHECK_INTERVAL_SECONDS = 10
MAX_BODY_LENGTH        = 1000        # Keep body short and clean
SEEN_IDS_FILE          = "seen_email_ids.json"

# ─────────────────────────────────────────────
#  🌐  BUILT-IN WEB SERVER (keeps Replit awake)
# ─────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Gmail Bot is running!")

    def log_message(self, format, *args):
        pass

def run_server():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()

# ─────────────────────────────────────────────


def load_seen_ids():
    if os.path.exists(SEEN_IDS_FILE):
        with open(SEEN_IDS_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_seen_ids(seen_ids):
    with open(SEEN_IDS_FILE, "w") as f:
        json.dump(list(seen_ids), f)


def decode_mime_words(s):
    if not s:
        return "(none)"
    parts = decode_header(s)
    decoded = []
    for part, enc in parts:
        if isinstance(part, bytes):
            decoded.append(part.decode(enc or "utf-8", errors="replace"))
        else:
            decoded.append(part)
    return "".join(decoded).strip()


def strip_html(text):
    """Remove all HTML tags and decode HTML entities."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Decode HTML entities like &amp; &nbsp; etc
    import html as html_module
    text = html_module.unescape(text)
    return text.strip()


def get_plain_body(msg):
    """
    Extract only plain text body.
    - Prefers text/plain parts
    - If only text/html exists, strips all HTML tags
    - Ignores attachments and images completely
    """
    plain_body = ""
    html_body  = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition  = str(part.get("Content-Disposition", ""))

            # Skip attachments and images entirely
            if "attachment" in disposition:
                continue
            if content_type.startswith("image/"):
                continue

            charset = part.get_content_charset() or "utf-8"

            if content_type == "text/plain":
                try:
                    plain_body = part.get_payload(decode=True).decode(charset, errors="replace")
                except:
                    pass

            elif content_type == "text/html" and not plain_body:
                try:
                    raw_html  = part.get_payload(decode=True).decode(charset, errors="replace")
                    html_body = strip_html(raw_html)
                except:
                    pass
    else:
        content_type = msg.get_content_type()
        charset = msg.get_content_charset() or "utf-8"

        try:
            raw = msg.get_payload(decode=True).decode(charset, errors="replace")
            if content_type == "text/html":
                plain_body = strip_html(raw)
            else:
                plain_body = raw
        except:
            pass

    # Use plain text first, fall back to stripped HTML
    body = plain_body.strip() if plain_body.strip() else html_body.strip()

    # Clean up excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)

    return body if body else "(no text content)"


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id":    TELEGRAM_CHAT_ID,
        "text":       text,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if not response.ok:
            print(f"[Telegram error] {response.status_code}: {response.text}")
    except requests.RequestException as e:
        print(f"[Telegram request failed] {e}")


def check_gmail(seen_ids):
    new_emails = []
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        if status != "OK":
            return new_emails

        email_ids = messages[0].split()

        for eid in email_ids:
            eid_str = eid.decode()
            if eid_str in seen_ids:
                continue

            status, msg_data = mail.fetch(eid, "(RFC822)")
            if status != "OK":
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    subject = decode_mime_words(msg.get("Subject", ""))
                    sender  = decode_mime_words(msg.get("From", ""))
                    date    = msg.get("Date", "")
                    body    = get_plain_body(msg)

                    new_emails.append({
                        "id":      eid_str,
                        "subject": subject,
                        "from":    sender,
                        "date":    date,
                        "body":    body
                    })

            seen_ids.add(eid_str)

        mail.logout()

    except imaplib.IMAP4.error as e:
        print(f"[IMAP error] {e}")
    except Exception as e:
        print(f"[Unexpected error] {e}")

    return new_emails


def format_telegram_message(email_data):
    """Format a clean, short, plain-text Telegram message."""
    sender  = html.escape(email_data["from"])
    subject = html.escape(email_data["subject"])
    date    = html.escape(email_data["date"])
    body    = html.escape(email_data["body"])

    # Truncate body if too long
    if len(body) > MAX_BODY_LENGTH:
        body = body[:MAX_BODY_LENGTH] + "...\n<i>(message truncated)</i>"

    return (
        f"📧 <b>New Email</b>\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"👤 <b>From:</b> {sender}\n"
        f"📌 <b>Subject:</b> {subject}\n"
        f"📅 <b>Date:</b> {date}\n"
        f"━━━━━━━━━━━━━━━━\n"
        f"{body}"
    )


def main():
    # Start web server for UptimeRobot
    print("🌐 Starting web server on port 8080...")
    threading.Thread(target=run_server, daemon=True).start()
    print("✅ Web server running!\n")

    print("✅ Gmail → Telegram Bot started!")
    print(f"   Checking every {CHECK_INTERVAL_SECONDS} seconds...\n")

    seen_ids = load_seen_ids()

    if not seen_ids:
        print("📂 First run: indexing existing emails (won't forward old ones)...")
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            mail.select("inbox")
            status, messages = mail.search(None, "ALL")
            if status == "OK":
                for eid in messages[0].split():
                    seen_ids.add(eid.decode())
            mail.logout()
            save_seen_ids(seen_ids)
            print(f"   Indexed {len(seen_ids)} existing emails. Watching for new ones...\n")
        except Exception as e:
            print(f"[Error during init] {e}")

    send_telegram_message("🤖 <b>Gmail Bot is now active!</b>\nI'll forward new emails to you here.")

    while True:
        try:
            new_emails = check_gmail(seen_ids)
            for email_data in new_emails:
                message = format_telegram_message(email_data)
                send_telegram_message(message)
                print(f"[Forwarded] {email_data['subject']} — from {email_data['from']}")
                save_seen_ids(seen_ids)

        except KeyboardInterrupt:
            print("\n👋 Bot stopped.")
            break
        except Exception as e:
            print(f"[Loop error] {e}")

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
