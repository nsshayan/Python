#!/usr/bin/env python
import poplib
import sys

if len(sys.argv) < 4:
    print("usage: %s host username password" % sys.argv[0])
    sys.exit(-1)
    

mail = poplib.POP3(sys.argv[1])
mail.user(sys.argv[2])
mail.pass_(sys.argv[3])

(code, data, size) = mail.list()
for i in data:
    n, size = i.split()
    
    (code, data, size) = mail.retr(int(n))
    for line in data:
        if "From" in line or "Subject" in line: print(line)
    
    print("-" * 40)



