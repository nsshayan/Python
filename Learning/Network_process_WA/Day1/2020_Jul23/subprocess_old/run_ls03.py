from subprocess import Popen, PIPE

p = Popen(["ls", "-l"], stdout=PIPE)

for line in p.stdout:
    print(line.upper())

p.wait()

