import smtplib
from email.message import EmailMessage
import ssl  # safeguarding sensitive data between two clients

email_sender = 'sender@gmail.com'
email_password = 'password'

email_receiver = 'receiver@gmail.com'

subject = '[Cesar] Testing Email Sending with Python'

body = '''
Hey brother man, 

I have finally got this to work. Just know that I am sending this email
to you via python. Just a single click. 

With my best regards,
Cesar [The Analyst]
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


