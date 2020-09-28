from subprocess import Popen

#p = Popen(["ls", "/bin"])
p = Popen("ls /bin", shell=True)

print("Popen object created: p =", p)

ret = p.wait()
print("Command completed: exitcode =", ret)
