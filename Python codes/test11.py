import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Email credentials
email = ''
password = ''

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = email
msg['Subject'] = 'Automated Email from Python SMTP Protocol'

# Attach the image
with open("C:\Study Material\Python Study\\pexels-bri-schneiter-346529.jpg", 'rb') as f:
    image_data = f.read()
image = MIMEImage(image_data)
image.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(image)
# HTML content of the email
html_content = """
<html>
<body>
<h1>Hello,</h1>
<p>This message is from an automated Python SMTP Protocol!</p>
<p>Please do not reply to this email.</p>
<img src="cid:image.jpg">
</body>
</html>
"""

# Attach the HTML content
html_part = MIMEText(html_content, 'html')
msg.attach(html_part)

# Connect to the SMTP server and send the email
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(email, password)
smtp.send_message(msg)
smtp.quit()
