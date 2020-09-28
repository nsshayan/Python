from subprocess import Popen, PIPE

#p = Popen(["ls", "-l", "/usr"], stdout=PIPE, universal_newlines=True)
p = Popen("ifconfig", stdout=PIPE, encoding="utf8")

#for line in p.stdout:
#    if "inet " in line:
#        print(line.split()[1])

ipaddrs = [ line.split()[1] for line in p.stdout if "inet " in line ]
print(ipaddrs)