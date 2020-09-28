from subprocess import Popen

#p = Popen("ls /bin | wc -l", shell=True) # /bin/sh -c "ls /bin | wc -l"
p = Popen(["ls", "/bin"])
print("Launched ls command: p =", p, "Pid =", p.pid)

ret = p.wait()
print("ls exited with ret =", ret)