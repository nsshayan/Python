from subprocess import Popen, PIPE


p = Popen(["ls", "-l", "/", "/dfsfd"], stdout=PIPE, stderr=PIPE,
          # universal_newlines=True)
          # encoding="utf8")
          text=True)

for line in p.stdout:
    # print(line.upper())
    print(str(line, "utf8").upper())
print("---------------------")
for line in p.stderr:
    print(line.upper())
