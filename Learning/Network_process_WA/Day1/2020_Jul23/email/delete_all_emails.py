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
        result = mail.dele(msg_num)
        print(f"Msg {msg_num}: {result}")


