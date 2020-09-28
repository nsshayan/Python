from telnetlib import Telnet

host = "192.168.56.105"
port = 2023
username = b"pythonista\n"
password = b"w3lc0me\n"

prompt = b"[pythonista@archvm ~]$"

tn = Telnet(host, port)
tn.set_debuglevel(7)

tn.read_until(b"login:")
tn.write(username)

tn.read_until(b"Password:")
tn.write(password)

tn.read_until(prompt)
tn.write(b"uname -a\n")

output = tn.read_until(prompt)
tn.write(b"exit\n")
tn.close()
print(str(output, "utf8"))