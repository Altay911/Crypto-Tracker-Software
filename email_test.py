import smtplib
from email.message import EmailMessage

sender_email = "educationvideos13@gmail.com"
receiver_email = "educationvideos13@gmail.com"
app_password = "vfazainuqftjzkgs"

msg = EmailMessage()
msg['Subject'] = "Crypto bot alert!"
msg['From'] = sender_email
msg['To'] = receiver_email

msg.set_content("Fuck Yeah your code is workinggg")

print("connecting to google servers...")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("email sent to your inbox!")