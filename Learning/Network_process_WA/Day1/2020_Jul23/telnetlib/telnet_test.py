from telnetlib import Telnet

t = Telnet("192.168.56.101", 2023)
t.set_debuglevel(1)

t.read_until(b"login: ")
t.write(b"pythonista\n")

t.read_until(b"Password: ")
t.write(b"welcome\n")

t.read_until(b"$ ")
t.write(b"ls /etc\n")
output = t.read_until(b"$ ")

print(str(output, "utf8"))

t.close()



