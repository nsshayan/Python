from subprocess import Popen, PIPE

#ifconfig = Popen("ifconfig", stdout=PIPE, universal_newlines=True)
ifconfig = Popen("ifconfig", stdout=PIPE, encoding="utf8")

for line in ifconfig.stdout:
    if "IPv4" in line:
        print(line.split()[-1])