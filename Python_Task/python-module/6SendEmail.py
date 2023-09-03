import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr

# Email configuration
sender_email = 'your_email@example.com'
sender_name = 'Your Name'
receiver_email = 'recipient@example.com'
subject = 'Subject of the Email'
message = 'Hello, this is the body of the email.'

# Create the MIMEText object
msg = MIMEMultipart()
msg['From'] = formataddr((sender_name, sender_email))
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Connecting to the SMTP server
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_username'
smtp_password = 'your_password'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    # Sending the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print('Error:', e)
finally:
    server.quit()
