import imaplib
import email

def create_client(username, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('devremoterm@gmail.com', 'termmyremote')
    mail.select('inbox')
    return mail


class GmailSender:

    def __init__(self, login, password):
        self.client = create_client(login, password)
    
    def fetch_new(self):
        result, data = self.client.search(None, 'ALL')
  

mail = imaplib.IMAP4_SSL('imap.gmail.com')

mail.login('devremoterm@gmail.com', 'termmyremote')
mail.select('inbox')

result, data = mail.search(None, 'ALL')

for num in data[0].split():
    typ, message = mail.fetch(num, '(RFC822)')

    message = message[0][1]
    message = message.decode(encoding='UTF-8')

    email_object = email.message_from_string(message)

    print(num)
    if email_object.is_multipart():
        # for payload in email_object.get_payload():
        #     print(payload.get_payload())
        print(email_object.get_payload()[0].get_payload())
    else:
        print(email_object.get_payload())

mail.close()
mail.logout()
