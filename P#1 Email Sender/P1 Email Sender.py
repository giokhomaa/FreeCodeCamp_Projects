from email.message import  EmailMessage
from app2 import password #მეორე ფაილში შევინახეთ პაროლი და იქიდან დავაიმპორტეთ, რათა უფრო უსაფრთხო იყოს
import ssl  #ssl ფუნქციის საშუალებით გავდივართ ავტომატურ დალოგინებას მეილზე პაროლით
import smtplib

email_sender = 'giorgahoma@gmail.com'
email_password = password

email_receiver = 'giokhomaa@gmail.com'

subject = 'Hello, this is email sender'
body = '''
Gamarjoba, this is Python automatic message
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())