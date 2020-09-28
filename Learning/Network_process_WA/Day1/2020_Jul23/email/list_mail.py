#!/usr/bin/env python
from poplib import POP3
import sys


mail = POP3("mail.chandrashekar.info")
mail.user("testuser")
mail.pass_("w3lc0me")


(code, mail_list, size) = mail.list()
for entry in mail_list:
    n, size = entry.split()
    (code, data, size) = mail.retr(int(n))
    print("-" * 40)
    for line in data:
        if "From" in line: print(line)
        if "Subject" in line: print(line)
    print("=" * 40)

    
