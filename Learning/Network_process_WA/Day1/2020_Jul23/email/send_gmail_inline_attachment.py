import cgi
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.header         import Header
import os
import smtplib
from email.MIMEBase import MIMEBase
from email import Encoders

with open('credentials.csv', 'rb') as f:
    gmail_user = f.readline().strip().split(',')[1]
    gmail_pwd = f.readline().strip().split(',')[1]

def attach_image(img_dict):
    with open(img_dict['path'], 'rb') as file:
    msg_image = MIMEImage(file.read(), name = os.path.basename(img_dict['path']))
    msg_image.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
    return msg_image

def attach_file(filename):
    part = MIMEBase('application', 'octect-stream')
    part.set_payload(open(filename, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=%s' % os.path.basename(filename))
    return part

def generate_email(gmail_user, to_list, data_path_1, data_path_2,img1,img2):
    msg = MIMEMultipart('related')
    msg['Subject'] = Header(u'Images and Words', 'utf-8')
    msg['From'] = gmail_user
    msg['To'] = ','.join(to_list)
    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(u'Image not working - maybe next time', 'plain', 'utf-8')
    msg_alternative.attach(msg_text)
    msg.attach(msg_alternative)
    msg_html = u'<h1>Some images coming up</h1>'
    msg_html += u'<h3>Image 1</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img1['title'], quote=True), **img1)
    msg_html += u'<h3>Image 2</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img2['title'], quote=True), **img2)
    msg_html = MIMEText(msg_html, 'html', 'utf-8')
    msg_alternative.attach(msg_html)
    msg.attach(attach_image(img1))
    msg.attach(attach_image(img2))
    msg.attach(attach_file(data_path_1))
    msg.attach(attach_file(data_path_2))
    return msg

def send_email(msg, gmail_user, gmail_pwd, to_list):
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to_list, msg.as_string())
    mailServer.quit()

img1 = dict(title = 'Image 1', path = 'test_image_1.png', cid = str(uuid.uuid4()))
img2 = dict(title = 'Image 2', path = 'test_image_2.png', cid = str(uuid.uuid4()))

email_msg = generate_email(gmail_user, ['recipient@email.com'], 'test_data.txt', 'test_data_2.txt', img1, img2)
send_email(email_msg, gmail_user, gmail_pwd, ['recipient@email.com'])

