from smtplib import SMTP
import imghdr

from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'My photo'

msg['From'] = "scary.pythonista@gmail.com"
msg['To'] = "testuser@chandrashekar.info"
msg.preamble = 'My photo'

filename = "/Users/chandrashekar/Documents/chandrashekar_babu.jpg"
with open(filename, 'rb') as fp:
    img_data = fp.read()
    
msg.add_attachment(img_data, maintype='image',
                    subtype=imghdr.what(None, img_data))

# Send the email via our own SMTP server.
with SMTP('smtp.gmail.com', 587) as s:
    s.ehlo()
    s.starttls()
    s.login("scary.pythonista@gmail.com", "slashprog")
    s.send_message(msg)
