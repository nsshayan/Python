from subprocess import Popen, PIPE

p = Popen(["/sbin/ifconfig"], stdout=PIPE)

for line in p.stdout:
    if "IPv4" in line:
        print(line.strip().split(":")[-1])

#[ line.strip().split()[1] for line in p.stdout if "inet" in line ]
