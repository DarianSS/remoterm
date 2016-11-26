import smtplib
from email.mime.text import MIMEText

class GmailSender:
    
    def __init__(self, login, password):
        self.client = smtplib.SMTP('smtp.gmail.com:587')
        self.login = login

        self.client.starttls()
        self.client.login(self.login, password)

    def send_mail(self, mail):
        mime_text = MIMEText(mail['body'])
        mime_text['Subject'] = mail['subject']
        mime_text['From'] = self.login
        mime_text['To'] = mail['to']
        self.client.sendmail(self.login, mime_text['To'], str(mime_text))

