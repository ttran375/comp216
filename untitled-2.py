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

html_m = "<html><body><b>Hello</b><br>Testing HTML Email</br>--COMP216</body></html>"


email_content = MIMEText(html_m, "html")
email_content["From"] = EMAIL_ACC
email_content["To"] = RECPT
email_content["Subject"] = "Testing HTML Email Message"


try:
  with smtplib.SMTP(SERVER, PORT) as smtp:
except:

else: