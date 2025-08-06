#eyftsezccidbekpt

from email.message import EmailMessage
import ssl
import smtplib

def send_email(cont_path, mail_receiver):

    mail_sender = 'preethinikita21@gmail.com'
    mail_password = 'wllbfpinfcscqunk'

    
    subject = 'Ticket Received for Traffic Rule Violation'

    em = EmailMessage()
    em['From'] = mail_sender
    em['To'] = mail_receiver
    em['subject'] = subject

    with open(cont_path, 'rb') as content_file:
        content = content_file.read()
        em.add_attachment(content, maintype='application', subtype='docx', filename='ticket.docx')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mail_sender, mail_password)
        smtp.send_message(em)




