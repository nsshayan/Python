from subprocess import Popen, PIPE

p = Popen("ls", stdout=PIPE, encoding="utf8")

#p = Popen("ls", stdout=PIPE, universal_new_lines=True)

for line in p.stdout:
    print(line.upper())
    