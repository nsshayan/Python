from subprocess import Popen, PIPE

p = Popen(["ls", "-l", "/usr", "/opt"],
          #universal_newlines=True,
          #encoding="utf8",
          stdout=PIPE)

#output = str(p.stdout.read(), "utf8")
#print(output)
for line in p.stdout:
    print(line.upper())

