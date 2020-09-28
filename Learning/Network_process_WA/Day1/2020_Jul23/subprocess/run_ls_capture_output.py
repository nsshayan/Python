from subprocess import Popen, PIPE


p = Popen(["ls", "-l", "/usr"], stdout=PIPE)

#for line in p.stdout:
#    print(str(line.upper(), "utf8"))

output = p.stdout.read()
print(output.upper())
ret = p.wait()
print("ls completed with exitcode =", ret)
