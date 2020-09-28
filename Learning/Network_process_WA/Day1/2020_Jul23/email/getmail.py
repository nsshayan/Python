#!/usr/bin/env python
import poplib
import sys

if len(sys.argv) < 5:
    print("usage: %s host username password mailnum" % sys.argv[0])
    sys.exit(-1)
    

mail = poplib.POP3(sys.argv[1])
mail.user(sys.argv[2])
mail.pass_(sys.argv[3])


(code, data, size) = mail.retr(int(sys.argv[4]))
for line in data:
    print(line)
    
