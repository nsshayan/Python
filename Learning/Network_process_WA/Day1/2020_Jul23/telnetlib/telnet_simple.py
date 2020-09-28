from telnetlib import Telnet
from time import sleep

HOST = "192.168.56.101"
user = b"pythonista"
password = b"welcome123"

tn = Telnet(HOST)
#tn.set_debuglevel(7)

tn.read_until(b"login: ")
tn.write(user + b"\r")
tn.expect([])
#tn.expect(["login.*:", "Login.+:"])
tn.read_until(b"Password:", timeout=5)
tn.write(password + b"\r")

#tn.read_until("?", timeout=5)
#tn.write("vt100\r")

tn.read_until(b"[pythonista@archvm ~]$ ")
#tn.write("cat /proc/cpuinfo\r")

tn.write(b"uname -a\r")

output = tn.read_until(b"[pythonista@archvm ~]$ ")

print("-" * 40)
print(str(output, "utf8"))
print("-" * 40)
print("Interacting...")

tn.interact()
print("Back to python script...")
tn.write(b"exit\r")
