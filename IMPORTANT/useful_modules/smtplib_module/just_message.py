import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = str(input('Sender mail: '))
sender_password = str(input('Enter a password: '))
receiver = str(input('Receiver mail: '))
topic = str(input('Message topic: '))
message = str(input('Main text: '))
count = int(input('\nMessage quantity: '))

def send_mail():
    try:
        msg = MIMEMultipart()
        msg['Subject'] = topic
        msg['From'] = sender
        msg['To'] = receiver
        msg.attach(MIMEText(message, 'plain'))

        text = msg.as_string()

        with smtplib.SMTP('smtp.gmail.com:587') as server:
            server.starttls()
            server.login(sender, sender_password)
            server.sendmail(sender, receiver, text)

        print('Mail was successfully sent!')
    except Exception as ex:
        print('Failed - ', ex)

if __name__ == '__main__':
    for _ in range(1, count + 1):
        send_mail()

input('Type something to exit: ')
