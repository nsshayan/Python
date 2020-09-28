from subprocess import Popen, PIPE

p = Popen("ifconfig", stdout=PIPE)

ip_addresses = [ str(line.split()[1], "utf8") for line in p.stdout if b"inet" in line ]
print(ip_addresses)


