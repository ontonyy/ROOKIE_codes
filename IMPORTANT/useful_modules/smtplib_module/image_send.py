import smtplib
from email.message import EmailMessage
import imghdr

sender = str(input('Your mail: '))
sender_password = str(input('Your password: '))
receiver = str(input('Receiver mail: '))
topic = str(input('Topic: '))
message = str(input('MAIN message: '))

msg = EmailMessage()
msg['Subject'] = topic
msg['From'] = sender
msg['To'] = receiver
msg.set_content(message)

for c in range(1, 4):
    with open(f'C:\main_modules\my_modules\Disain(tkinter, kivy, pyqt)\images/try{c}.png', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, sender_password)
    server.send_message(msg)
