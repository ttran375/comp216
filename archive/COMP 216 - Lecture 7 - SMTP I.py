import smtplib

SMTP_SERVER = 'smtp.gmail.com'  #Identify SMTP Server
PORT = 587  #SMTP TLS Port
EMAIL_ACC = 'USER_EMAIL'  #Update with Gmail account
PASSWORD = 'PASSWORD'  #Create and use Google App Password 

RECPT_EMAIL = 'RECIPIENT EMAIL[S]'  #String encompassing one or more email addresses where each email address is separated by ','

#Create a template for email message and relevant properties; Note: remember to start all emails with "\" to ensure the proper creation of the template
message = f"""\  
From: {EMAIL_ACC}
To: {RECPT_EMAIL}
Subject: SMTP Test

Testing new Python app with config file over TLS.
"""

try:
    with smtplib.SMTP(SMTP_SERVER, PORT) as smtp:  #Use the WITH statement to create a runtime context manager and ensure the proper acquisition and release of resources
        smtp.starttls()  #Use SMTP connection in Transport Layer Security (TLS) mode
        smtp.login(EMAIL_ACC, PASSWORD)
        smtp.sendmail(EMAIL_ACC, RECPT_EMAIL, message)  #Ensure message parameter is a string 
except Exception as e:
    print(f'Error: {e}')
else:
    print('Email sent successfully')

