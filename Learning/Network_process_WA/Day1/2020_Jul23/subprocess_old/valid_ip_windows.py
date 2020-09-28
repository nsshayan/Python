from subprocess import Popen, PIPE

p = Popen("ipconfig", stdout=PIPE)

for line in p.stdout:
    if "IP Address" in line:
        print(line.split(":")[1])

p.wait()

