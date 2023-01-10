
from email.message import EmailMessage
import smtplib

email_sender = 'yonitermi@gmail.com'
email_password = 'mgyivqyqhksennvd'
email_reciever = 'yonitermi@gmail.com'

subject =  'check '
body = """
whats up github?
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_sender , email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())