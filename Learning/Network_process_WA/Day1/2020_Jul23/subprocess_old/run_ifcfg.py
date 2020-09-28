from subprocess import Popen, PIPE

child_proc = Popen(["ifconfig"], stdout=PIPE)

for line in child_proc.stdout:
    if "inet " in line:
        print(line.split()[1])
