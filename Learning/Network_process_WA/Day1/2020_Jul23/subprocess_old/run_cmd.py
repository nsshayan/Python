from subprocess import Popen, PIPE

cmd = Popen("ls", stdout=PIPE)

for line in cmd.stdout:
    print(line.upper())


