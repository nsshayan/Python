from subprocess import Popen, PIPE

child = Popen("/sbin/ifconfig", stdout=PIPE, stderr=PIPE)

for line in child.stdout:
    #if "inet " in line: print line.split()[1]
    if "IPv4" in line: print(line.split(": ")[-1])

child.wait()

