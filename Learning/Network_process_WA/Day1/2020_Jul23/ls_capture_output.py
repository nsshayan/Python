from subprocess import Popen, PIPE

p = Popen(["ls", "-l"], stdout=PIPE)

for line in p.stdout:
    #print(line.upper())
    fields = line.split()
    if len(fields) > 4:
        print(fields[4])

