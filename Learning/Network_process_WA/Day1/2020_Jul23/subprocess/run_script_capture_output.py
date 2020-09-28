from subprocess import Popen, PIPE


p = Popen("./slow_script.sh", stdout=PIPE)

for line in p.stdout:
    print(str(line.upper(), "utf8"))

#output = p.stdout.read()
#print(output.upper())
ret = p.wait()
print("ls completed with exitcode =", ret)
