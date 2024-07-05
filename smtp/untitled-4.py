from email.mime.base import MIMEBase
import smtplib
from dotenv import load_dotenv
from email import encoders
import os
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart


load_dotenv()


SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ACC = "cen.comp216@gmail.com"
PASSWORD = os.getenv("PASSWORD")

RECPT = "cen.comp216@gmail.com"

html_m = (
    "<html><body><b>Hello</b><br>Email with attachment</br>Download PDF.</body></html>"
)
h_email_content = MIMEText(html_m, "html")

txt_m = "Hello Email with Attachment! Download PDF."
t_email_content = MIMEText(txt_m, "plain")

filename = "dictionary.pdf"

with open(filename, "rb") as upload_file:
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(upload_file.read())

encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', f'attachment; filename={filename}')


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
