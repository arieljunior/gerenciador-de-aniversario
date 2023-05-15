import smtplib
from email.mime.text import MIMEText
from string import Template
from email.mime.multipart import MIMEMultipart
import os 
from dotenv import load_dotenv
from email_validator import validate_email

load_dotenv()

EMAIL_LOGIN = os.getenv('SMTP_USER')
PASSWORD_LOGIN = os.getenv('SMTP_PASSWORD')
HOST = os.getenv('SMTP_HOST')
PORT = os.getenv('SMTP_PORT')
TEMPLATE_EMAIL_PATH= os.getenv('TEMPLATE_EMAIL_PATH')

def sendEmailBirthday(receivers: list):
    countSend = 0
    try:
        with open(TEMPLATE_EMAIL_PATH, 'r', encoding='utf-8') as template_file:
            template_file_content = Template(template_file.read())

        server = smtplib.SMTP(HOST, PORT)
        server.starttls()
        server.login(EMAIL_LOGIN, PASSWORD_LOGIN)

        for receiver in receivers:
            print(receiver)
            content = template_file_content.substitute(PERSON_NAME=receiver.fullname)
            msg = MIMEMultipart()
            msg['From'] = EMAIL_LOGIN
            msg['To'] = receiver.email
            msg['Subject'] = "Parabéns"
            msg.attach(MIMEText(content, 'plain'))
            server.send_message(msg)
            del msg
            countSend +=1

        server.quit()
    except Exception as ex:
        print(ex)
    finally:
        return countSend

def isValidEmail(email):
    try:
        validate_email(email)
        return True
    except:
        return False