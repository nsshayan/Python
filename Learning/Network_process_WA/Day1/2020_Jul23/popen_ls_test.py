from subprocess import Popen

#p = Popen(["ls",  "-l"])
#p = Popen("ls -l", shell=True)
p = Popen(["/bin/bash", "-c", "ls -l"])

print("Process launched: p =", p)
ret = p.wait()
print("Process exited: ret =", ret)
