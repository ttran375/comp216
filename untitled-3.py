import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()


SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ACC = "cen.comp216@gmail.com"
PASSWORD = os.getenv("PASSWORD")

RECPT = "cen.comp216@gmail.com"

html_m = "<html><body><b>Hello</b><br>Testing HTML Email</br>--COMP216</body></html>"
h_email_content = MIMEText(html_m, "html")

txt_m = "Hello Testing HTML Email --COMP216"
t_email_content = MIMEText(txt_m, "plain")

email_msg = MIMEMultipart()
email_msg["From"] = EMAIL_ACC
email_msg["To"] = RECPT
email_msg["Subject"] = "Testing HTML Email Message V2"

email_msg.attach(h_email_content)
email_msg.attach(t_email_content)

try:
    with smtplib.SMTP(SERVER, PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ACC, PASSWORD)
        smtp.sendmail(EMAIL_ACC, RECPT, email_msg.as_string())
except Exception as e:
    print(f"Error: {e}")
else:
    print("Success")
