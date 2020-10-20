import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'W3bh4ck'
email['to'] = 'example@gmail.com'
email['subject'] = 'Email subject'

email.set_content(html.substitute({'name': 'uche'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('source email', 'password')
	smtp.send_message(email)
	print('email sent')
