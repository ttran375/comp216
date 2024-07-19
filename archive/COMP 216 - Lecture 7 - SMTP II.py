import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'  #Identify SMTP Server
PORT = 587  #SMTP TLS Port
EMAIL_ACC = 'USER_EMAIL'  #Update with Gmail account
PASSWORD = 'PASSWORD'  #Create and use Google App Password 

RECPT_EMAIL = 'RECIPIENT EMAIL[S]'  #String encompassing one or more email addresses where each email address is separated by ','

#Create a template HTML for an email message; Note: remember to capture HTML structure and content as a string
html = '<html><body><b>Hello</b><br>Testing with HTML Content<br>--COMP216</body></html>'

email_content = MIMEText(html, 'html')  #MIME object extends the email format to support non-ASCII characters, HTML content and other attachments (e.g., audio, video, PDF, etc.); MIMEText object allows for the creation of HTML/plain-text content
email_content['From'] = EMAIL_ACC
email_content['To'] = RECPT_EMAIL
email_content['Subject'] = 'Testing HTML Message'


try:
    with smtplib.SMTP(SMTP_SERVER, PORT) as smtp:  #Use the WITH statement to create a runtime context manager and ensure the proper acquisition and release of resources
        smtp.starttls()  #Use SMTP connection in Transport Layer Security (TLS) mode
        smtp.login(EMAIL_ACC, PASSWORD)
        smtp.sendmail(EMAIL_ACC, RECPT_EMAIL, email_content.as_string())  #Ensure message parameter is a string 
except Exception as e:
    print(f'Error: {e}')
else:
    print('Email sent successfully')

 