import sys
from telnetlib import Telnet

HOST = "192.168.43.139"
user = "joe" 
password = "w3lc0me" 

tn = Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\r")

tn.read_until("Password:", timeout=5)
tn.write(password + "\r")

tn.read_until("?", timeout=5)
tn.write("vt100\r")

tn.read_until(r"> ")
tn.write("sudo /etc/init.d/apache2 stop\r")

print("OUTPUT: ", tn.read_until(r"> "))

tn.write("exit\r")


