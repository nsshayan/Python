import sys
from telnetlib import Telnet
import re

HOST = "192.168.56.105"
PORT = 2023
user = b"pythonista\r"
password = b"welcome\r"

tn = Telnet(HOST, PORT)
#tn.set_debuglevel(7)

tn.read_until(b"login: ")
tn.write(user)

tn.read_until(b"Password:")
tn.write(password)

tn.read_until(b"$ ")
tn.write(b"uname -a\r")

print(str(tn.read_until(b"$ "), "utf8"))

tn.interact()
print("Back to telnet program...")
tn.write(b"exit\r")
