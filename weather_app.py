import smtplib
from email.message import EmailMessage

# Create the email
msg = EmailMessage()
msg['Subject'] = '🚨 Weather Alert: Temp is Rising!'
msg['From'] = 'colinsony22@gmail.com'
msg['To'] = 'kevinsony2003@gmail.com'
msg.set_content('The temperature just passed your daily max threshold.')

# Connect to Gmail's SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('colinsony22@gmail.com', 'xsdp cfxl drxx kxdo')  # Use app password here
    smtp.send_message(msg)
