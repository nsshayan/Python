from subprocess import Popen, PIPE

with Popen("ls", stdout=PIPE, universal_newlines=True) as p:
    for line in p.stdout:
        print(line.upper())
