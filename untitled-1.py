import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText

load_dotenv()


SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ACC = "cen.comp216@gmail.com"
PASSWORD = os.getenv("PASSWORD")

RECPT = "cen.comp216@gmail.com"

html_m = "<h1><body><b>Hello</b>--COMP216</body></h1>"

email_content = MIMEText(html_m, "html")
email_content["From"] = EMAIL_ACC
email_content["To"] = RECPT
email_content["Subject"] = "COMP216 HTML Email"

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
        smtp.sendmail(EMAIL_ACC, RECPT, email_content.as_string())
except Exception as e:
    print(f"Error: {e}")
else:
    print("Success")
