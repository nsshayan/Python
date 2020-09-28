import smtplib

msg_format = """To: {", ".join(to_addresses)}
Subject: {subject}

{message}
"""

def send_gmail(gmail_user, gmail_passwd, to_list, subject, message):
    gmail_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_smtp.ehlo()
    gmail_smtp.starttls()
    gmail_smtp.ehlo()
    gmail_smtp.login(gmail_user, gmail_passwd)
    msg = msg_format(to_addresses=to_list, subject=subject, message=message)

    r = gmail_smtp.sendmail(gmail_user, to_list, msg)
    gmail_smtp.quit()
    return r

if __name__ == '__main__':
    from getpass import getpass
    gmail_user_name = input("Enter gmail id: ")
    gmail_password = getpass("Enter gmail password: ")

    to_list = input("Enter recipients separated by space: ").split()
    subject = input("Enter subject: ")
    message = input("Enter message: ")

    r = send_gmail(gmail_user_name, gmail_password, to_list, subject, message)
    print(r)

