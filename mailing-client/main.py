import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password f.read()

server.login('test@gmail.com' password)

msg = MIMEMultipart()
msg['From'] = 'MyName'
msg['To'] = 'ToPerson@gmail.com'
msg['Subject'] = 'Just A Test'