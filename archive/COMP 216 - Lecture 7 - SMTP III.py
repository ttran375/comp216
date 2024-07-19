import smtplib

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


SMTP_SERVER = 'smtp.gmail.com'  #Identify SMTP Server
PORT = 587  #SMTP TLS Port
EMAIL_ACC = 'USER_EMAIL'  #Update with Gmail account
PASSWORD = 'PASSWORD'  #Create and use Google App Password 

RECPT_EMAIL = 'RECIPIENT EMAIL[S]'  #String encompassing one or more email addresses where each email address is separated by ','


email_content = MIMEMultipart()  #MIME object extends the email format to support non-ASCII characters, HTML content and other attachments (e.g., audio, video, PDF, etc.); MIMEMultipart is utilized when the email is composed of multiple components (e.g., HTML and attachment)  
email_content['From'] = EMAIL_ACC
email_content['To'] = RECPT_EMAIL
email_content['Subject'] = 'Testing HTML Message with Attachment'

#Create a template HTML for an email message; Note: remember to capture HTML structure and content as a string
html = '<html><body><b>Hello</b><br>Testing with HTML Content and attachment<br>--COMP216</body></html>'
email_content.attach(MIMEText(html, 'html'))  #Attach HTML content to MIMEMultipart object

filename = 'PATH or FILENAME'
with open(filename, 'rb') as upload_file:  #Select and open the file in binary read mode (used for most file types -e.g., PDF, JPG, etc.) 
    attachment = MIMEBase('application', 'octet-stream')  #MIME object to create a base class for a variety of objects such as file attachments; ('application', 'octet-stream') paramaters used for setting content types associated with binary files
    attachment.set_payload(upload_file.read())
    
encoders.encode_base64(attachment)  #Encode the binary data from file as a base64 text
attachment.add_header(
    'Content-Disposition',
    f'attachment; filename= {filename}',
)  #Establish header properties to specify the inclusion of an attachment
email_content.attach(attachment)  #Attach PDF content to MIMEMultipart object


try:
    with smtplib.SMTP(SMTP_SERVER, PORT) as smtp:  #Use the WITH statement to create a runtime context manager and ensure the proper acquisition and release of resources
        smtp.starttls()  #Use SMTP connection in Transport Layer Security (TLS) mode
        smtp.login(EMAIL_ACC, PASSWORD)
        smtp.sendmail(EMAIL_ACC, RECPT_EMAIL, email_content.as_string())  #Ensure message parameter is a string 
except Exception as e:
    print(f'Error: {e}')
else:
    print('Email sent successfully')

 