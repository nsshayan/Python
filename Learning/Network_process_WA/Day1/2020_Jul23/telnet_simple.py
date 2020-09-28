from telnetlib import Telnet

tn = Telnet("192.168.56.105", 2023)
#tn.set_debuglevel(7)

tn.read_until(b"login: ")
tn.write(b"pythonista\n")

tn.read_until(b"word: ")
tn.write(b"welcome\n")

tn.read_until(b"$ ")
tn.write(b"cat /proc/loadavg\n")

output = tn.read_until(b"$ ")
tn.close()

print(str(output, "utf8"))
