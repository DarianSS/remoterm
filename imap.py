import imaplib
import email

class GmailGetter:

    def __init__(self, login, password):
        self.client = create_client(login, password)
        result, data = self.client.search(None, 'ALL')
        emails = data[0].split()
        self.current_size = emails[-1]

    def check_new(self):
        self.client.select('inbox')
        result, data = self.client.search(None, 'ALL')
        emails = data[0].split()
        new_size = emails[-1]

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
        index1 = from_field.find('<')
        index2 = from_field.find('>')
        sender = from_field[index1+1:index2]

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

# g = GmailGetter('devremoterm@gmail.com' , 'termmyremote')
# g.check_new()