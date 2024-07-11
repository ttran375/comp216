import poplib
from email.parser import Parser
import base64

SERVER = "pop.gmail.com"
PORT = 995
EMAIL_ACC = "cen.comp216@gmail.com"
PASSWORD = "lhuw tfza uvrh lplk"

mailbox = poplib.POP3_SSL(SERVER, PORT)
mailbox.user(EMAIL_ACC)
mailbox.pass_(PASSWORD)

response_code, mails, octet = mailbox.list()
# print(mails)

last_index = len(mails)
# print(last_index)

response_code_email, lines_emails, octet_email = mailbox.retr(last_index)
# print(lines_emails)

msg_content = b"\r\n".join(lines_emails).decode("utf-8")
# print(msg_content)

parsed_msg = Parser().parsestr(msg_content)

sender = parsed_msg.get("From")
recpt = parsed_msg.get("To")
date = parsed_msg.get("Date")
subject = parsed_msg.get("Subject")

print(sender, recpt, date, subject)

email_content = parsed_msg.get_payload()
print(email_content)

print(parsed_msg.is_multipart())
print(parsed_msg.get_content_type())


def multi_part_processor(msg):
    if msg.is_multipart():
        msg_list = msg.get_payload()
        for num, msg_obj in enumerate(msg_list):
            if msg.get_content_type() == "text/plain":
                with open("text_email.txt", "w") as body:
                    body.write(msg_obj.get_payload())

            elif msg.get_content_type() == "text/html":
                with open("html_email.txt", "w") as body:
                    body.write(msg_obj.get_payload())
