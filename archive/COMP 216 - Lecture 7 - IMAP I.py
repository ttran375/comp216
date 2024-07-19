import imaplib
import email
import email.header


SERVER = 'imap.gmail.com'  #Identify IMAP Server
PORT = 993  #IMAP TLS Port -- Not required
EMAIL_ACC = 'USER_EMAIL'  #Update with Gmail account
PASSWORD = 'PASSWORD'  #Create and use Google App Password 

mbox = imaplib.IMAP4_SSL(SERVER)  #It is possible to reconstruct the following operations using a context manager (with ... as ... construct) to ensure the acquisition and release of resources; Note: Call function without PORT values 
mbox.login(EMAIL_ACC, PASSWORD)

mbox.select('Inbox')  #IMAP supports folder or multiple mailbox structures; thus, requiring the selection of a folder/mailbox

response, index_vals = mbox.search(None, 'All')  #Specify search criteria based on the character set (can be set to None) and parameters in order to retrieve emails in the specified folder/mailbox (e.g., Retrieve all emails in the inbox folder)

response_mail, msg_raw = mbox.fetch(b'19', 'RFC822')  #Utilize decomposition to extract the response and raw email content when utilizing the IMAP FETCH method to return email with specified ID; Note: FETCH method requires the ID value of value in a binary string value and message format (typically: RFC822)

email_comp_raw = msg_raw[0][1]  #Retreive the message header and body components in a bytes-like object

email_comp = email.message_from_bytes(email_comp_raw)  #message object structure from a bytes-like object 

header_subject = email.header.decode_header(email_comp['Subject'])  #Extract and store header components based on pre-defined properties 
print(header_subject)



# Retrieving and processing the payload or email content can be completed in a similar manner to 'multi_part_processor()' function implemented in the POP protocol example