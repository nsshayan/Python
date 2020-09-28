from telnetlib import Telnet

connection = Telnet("192.168.169.1")
#connection.set_debug_level(7)

connection.read_until("login: ")
connection.write("hame\r")

connection.read_until("Password:", timeout=5)
connection.write("hame\r")

#tn.read_until("?", timeout=5)
#tn.write("vt100\r")

connection.read_until(r"# ")
connection.write("cat /proc/cpuinfo\r")

output = connection.read_until("# ")

connection.write("exit\r")

print("-" * 40)
print(output)
print("-" * 40)
