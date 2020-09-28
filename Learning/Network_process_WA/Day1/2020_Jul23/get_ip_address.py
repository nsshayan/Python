from subprocess import Popen, PIPE
import re
ip_pattern = re.compile(r"\s*(\d+(\.\d+){3})\s*", re.MULTILINE)

p = Popen("ifconfig", stdout=PIPE)
#for line in p.stdout:
#    if b"inet " in line:
#        print(str(line.split()[1], "utf8"))

#ip_addresses = [ str(line.split()[1], "utf8") \
#               for line in p.stdout         \
#               if b"inet " in line ]

#print(ip_addresses)

#for match in ip_pattern.finditer(str(p.stdout.read(), "utf8")):
#    print(match.group(1))
#    print(match)

print([ x[0] for x in ip_pattern.findall(str(p.stdout.read(), "utf8"))])