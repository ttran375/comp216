import poplib
from email.parser import Parser
import base64

SERVER = "pop.gmail.com"  # Identify POP Server
PORT = 995  # POP TLS Port
EMAIL_ACC = "USER_EMAIL"  # Update with Gmail account
PASSWORD = "PASSWORD"  # Create and use Google App Password

mailbox = poplib.POP3_SSL(
    SERVER, PORT
)  # It is possible to reconstruct the following operations using a context manager (with ... as ... construct) to ensure the acquisition and release of resources
mailbox.user(EMAIL_ACC)  # Note: Pass username and password credentials separately
mailbox.pass_(PASSWORD)

response, mails, octet = (
    mailbox.list()
)  # Utilize decomposition to extract the response, list of email ID/sizes, and octet unit size when utilizing the POP3 LIST method to return all new/available emails

last_index = len(
    mails
)  # Determine the last index value of the email to extract only the last email in the mailbox (Note: this email can be situated within the inbox, sent, deleted or another folder; POP3 does not recognize these as separate folder as all emails objects are treated as part of a centralized mailbox/folder)

response_mail, lines, octet_mail = mailbox.retr(
    last_index
)  # Utilize decomposition to extract the response, list of lines from email, and octet unit size when utilizing the POP3 RETR method to return email with specified ID
msg_content = b"\r\n".join(lines).decode(
    "utf-8"
)  # Concentate each line from the list to a string where each line is situated on a new line that starts at the leftmost column
parsed_msg = Parser().parsestr(msg_content)  # Pase out email object

sender = parsed_msg.get(
    "From"
)  # Extract and store values from the header and other email components using a dictionary-like GET method
recpt = parsed_msg.get("To")
subject = parsed_msg.get("Subject")
date = parsed_msg.get("Date")
print(
    f"""
From: {sender}
To: {recpt}
Subject: {subject}
Date: {date}
"""
)
print("\n\n")


def multi_part_processor(
    msg,
):  # Create a function to extract email payloads with multiple components (Note: simple text emails often have HTML and plain text components that are attached as separate components when the email is first created).
    if (
        msg.is_multipart()
    ):  # If the message payload has multiple components (returning a list of objects that an iterated through using a FOR loop)
        msg_parts = msg.get_payload()
        for num, part in enumerate(msg_parts):
            # print(num)  #Enable for only testing and debugging purposes
            # print(part.get_content_type())  #Enable for only testing and debugging purposes
            multi_part_processor(
                part
            )  # In most instances, email payloads have nested multi-part objects which can be processed by recursive calls to drive down to the individual email object

    else:  # Retrieve email payloads that have "easy to work" with content types or header values in order to extract and save relevant content
        if msg.get_content_type() == "text/plain":
            with open("message_body_new.txt", "w") as body:
                body.write(msg.get_payload())

        elif msg.get_content_type() == "text/html":
            with open("message_body_new.html", "w") as body:
                body.write(msg.get_payload())

        elif msg.get_content_disposition():
            with open(
                msg.get_filename(), "wb"
            ) as file:  # Retrieve filename from email header using .get_filename() method
                file.write(
                    base64.b64decode(msg.get_payload())
                )  # Convert base64 text to binary (bytes), then write the file
            print(msg.get_filename())

        else:  # Used to capture other content types that are not processed in the operation set above
            print(msg.get_content_type())


multi_part_processor(parsed_msg)
