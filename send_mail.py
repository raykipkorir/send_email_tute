import smtplib, os
from email.message import EmailMessage

#TLS -- 587
#SSL -- 465

#local SMTP Debugging server --> python -m smtpd -c DebuggingServer -n localhost:1025

smtp_server = "smtp.gmail.com"
port = "465"
sender_email = os.environ.get("EMAIL_ADDRESS")
receiver_email = "raykipkorir02@gmail.com"
password = os.environ.get("EMAIL_PASSWORD")

message = EmailMessage()
message["Subject"] = "This is test email"
message["From"] = sender_email
message["To"] = receiver_email

with open("index.html") as f:
    content = f.read()

message.add_alternative(content, subtype="html")

with open("ray.jpg", "rb") as img:
    file_data = img.read()
    file_name = img.name

message.add_attachment(file_data, maintype="image", subtype="jpg", filename=file_name)

with smtplib.SMTP(smtp_server, port) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(sender_email, password)
    # smtp.sendmail(sender_email, receiver_email, message)
    smtp.send_message(message)
