from subprocess import Popen, PIPE

p = Popen("/sbin/ifconfig", stdout=PIPE)

for line in p.stdout:
    if "inet addr" in line:
        print(line.split(":")[1].split(" ")[0])

p.wait()

