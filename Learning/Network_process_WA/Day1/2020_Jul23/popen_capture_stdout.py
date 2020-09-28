from subprocess import Popen, PIPE

command = "ls"

#p = Popen(command, stdout=PIPE, encoding="utf8")

#for line in p.stdout:
#    print(line.upper(), end="")

#p.wait()

with Popen(command, stdout=PIPE, encoding="utf8") as p:
    for line in p.stdout:
        print(line.upper(), end="")
