import time
import imap
import smtp
import config
import IO

def parse_email(body):
    separator = body.find('\n')

    if separator == -1:
        return None, None
    else:
        separator2 = body.find('\n', separator+1)
        return body[:separator-1], body[separator+1:separator2-1]

g_receiver = imap.GmailGetter(config.EMAIL, config.EMAIL_PASSWORD)

while (True):
    if (g_receiver.check_new()):
        email = g_receiver.get_new()

        to = email['sender']
        subject = 'Re: ' + email['subject']
        password, command = parse_email(email['body'])

        if password == config.APP_PASSWORD:

            shell = IO.ShellManager('/bin/bash')
            output = shell.getOutput(command)
            shell.exitProgram()

            print(output)

            new_mail = {'to' : to, 'subject' : subject, 'body' : output}

            g_sender = smtp.GmailSender(config.EMAIL, config.EMAIL_PASSWORD)
            g_sender.send_mail(new_mail)

    time.sleep(5)