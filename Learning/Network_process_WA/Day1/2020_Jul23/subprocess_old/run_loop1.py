from subprocess import Popen, PIPE

child = Popen("./loop.sh", stdout=PIPE)

for line in child.stdout:
    print("Captured line:", line.upper())


