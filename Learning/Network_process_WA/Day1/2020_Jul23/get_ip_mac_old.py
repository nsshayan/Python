from subprocess import Popen, PIPE

ifconfig = Popen("ifconfig", stdout=PIPE)
for line in ifconfig.stdout:
    line = str(line.strip(), "utf8")
    if "inet " in line:
        print(line.split()[1])


