import imaplib
import email

class GmailGetter:

    def __init__(self, login, password):
        self.client = create_client(login, password)
        result, data = self.client.search(None, 'ALL')
        self.current_size = (len(data[0]) + 1) / 2

    def check_new(self):
        self.client.select('inbox')
        result, data = self.client.search(None, 'ALL')
        new_size = (len(data[0]) + 1) / 2

        if new_size > self.current_size:
            self.current_size = new_size
            return True
        elif new_size < self.current_size:
            self.current_size = new_size
            return False
        else:
            return False

    def get_new(self):
        typ, message = self.client.fetch(str(int(self.current_size)), '(RFC822)')
        message = message[0][1]
        message = message.decode(encoding='UTF-8')

        email_body = email.message_from_string(message)

        from_field = email_body.get('From')
        delimiter1 = from_field.find('<')
        delimiter2 = from_field.find('>')
        sender = from_field[delimiter1:delimiter2]

        subject = email_body.get('Subject')

        if email_body.is_multipart():
            body = email_body.get_payload()[0].get_payload()
        else:
            body = email_body.get_payload()

        return {'sender' : sender, 'subject' : subject, 'body' : body}

def create_client(username, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.select('inbox')

    return mail

