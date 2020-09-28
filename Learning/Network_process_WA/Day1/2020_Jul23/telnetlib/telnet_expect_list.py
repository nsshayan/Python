from telnetlib import Telnet
from getpass import getpass

HOST = "192.168.56.105"

user = bytes(input("Enter username: "), "utf8")
password = bytes(getpass("Enter password: "), "utf8")

tn = Telnet(HOST, 2023)
#tn.set_debuglevel(7)

tn.read_until(b"login: ")
tn.write(user + b"\r")

tn.read_until(b"Password:", timeout=5)
tn.write(password + b"\r")

#tn.read_until("?", timeout=5)
#tn.write("vt100\r")


prompts = [b"\[pythonista@archvm ~\]\$ ",
           b"\[root@archvm ~\]# "]

index, match, buffer = tn.expect(prompts)
print("Matched {}, Match = {}, buffer = {}".format(
        index, match.group(0), buffer))

#tn.write("cat /proc/cpuinfo\r")

tn.write(b"uname -a\r")
index, match, buffer = tn.expect(prompts)
print("Matched {}, Match = {}, buffer = {}".format(
        index, match.group(0), buffer))


print("Back to python script...")
tn.write(b"exit\r")
