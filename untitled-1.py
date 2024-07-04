import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ACC = "cen.comp216@gmail.com"
PASSWORD = os.getenv("PASSWORD")

RECPT = "cen.comp216@gmail.com"

message = f"""\
From: {EMAIL_ACC}
To: {RECPT}
Subject: SMTP Test

Testing new Python app. First email!
"""

try:
    with smtplib.SMTP(SERVER, PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ACC, PASSWORD)
        smtp.sendmail(EMAIL_ACC, RECPT, message)
except Exception as e:
    print(f"Error: {e}")
else:
    print("Success")
