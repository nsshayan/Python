from subprocess import Popen, DEVNULL, STDOUT

#p = Popen("ls /bin | wc -l", shell=True) # /bin/sh -c "ls /bin | wc -l"
#with open("ls.out", "wb") as outfile, open("ls.err", "wb") as errfile:
#    p = Popen(["ls", "/bin", "/sdfsdf"], stdout=outfile, stderr=errfile)

p = Popen(["ls", "/bin", "/sdfsdf"], stdout=DEVNULL, stderr=STDOUT)

print("Launched ls command: p =", p, "Pid =", p.pid)

ret = p.wait()
print("ls exited with ret =", ret)