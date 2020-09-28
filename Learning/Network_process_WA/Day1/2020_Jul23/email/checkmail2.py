#!/usr/bin/env python
import poplib
import sys


mail = poplib.POP3("mail.chandrashekar.info")
mail.user("joe@chandrashekar.info")
mail.pass_("pythonista")

response_code, messages, octets = mail.list()
print("Response code:", response_code)

if b"OK" in response_code:
    for msg in messages:
        msg_num, size = (int(x) for x in msg.split())
        code, data, msg_size = mail.retr(msg_num)
        print(f"Msg {msg_num} reponse code: {code}")
        for line in data:
            if line.startswith(b"Subject") or line.startswith(b"From"):
                print(line)
        print("-" * 40)


