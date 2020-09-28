#!/usr/bin/env python
import smtplib
import sys

from_addr = input("From: ")
to_list = []

while True:
    to_addr = input("To: ")
    if not to_addr:
        break
    to_list.append(to_addr)

subject = input("Subject: ")
data = "Subject: " + subject + "\n\n"
print("Enter data, to finish, press Ctrl-D")
data += sys.stdin.read()

mail = smtplib.SMTP("mail.chandrashekar.info")
mail.sendmail(from_addr, to_list, data)


