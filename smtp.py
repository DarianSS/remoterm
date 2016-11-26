import smtplib

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()
server.sendmail('devremoterm@gmail.com', 'darian.sastre@gmail.com', 'Test')

server.close()
