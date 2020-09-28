from subprocess import Popen, PIPE

p = Popen("ifconfig", stdout=PIPE)
for line in p.stdout:
    if "inet " in line: print(line.split()[1])
