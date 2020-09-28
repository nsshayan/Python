from subprocess import Popen, PIPE

p = Popen(["ls", "-l", "/usr"], stdout=PIPE)

for line in p.stdout:
    print(line.upper())


