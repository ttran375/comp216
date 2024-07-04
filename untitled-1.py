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
