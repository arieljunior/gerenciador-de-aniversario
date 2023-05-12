import smtplib
from email.mime.text import MIMEText
from string import Template
from email.mime.multipart import MIMEMultipart

EMAIL_LOGIN = ""
PASSWORD_LOGIN = ""
HOST = 'smtp.gmail.com'
PORT = 587

def sendEmailBirthday(receivers: list):
    countSend = 0
    try:
        with open('template-email.txt', 'r', encoding='utf-8') as template_file:
            template_file_content = Template(template_file.read())

        server = smtplib.SMTP(HOST, PORT)
        server.starttls()
        server.login(EMAIL_LOGIN, PASSWORD_LOGIN)

        for receiver in receivers:
            print(receiver)
            content = template_file_content.substitute(PERSON_NAME=receiver.get("name"))
            msg = MIMEMultipart()
            msg['From'] = EMAIL_LOGIN
            msg['To'] = receiver.get("email")
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
