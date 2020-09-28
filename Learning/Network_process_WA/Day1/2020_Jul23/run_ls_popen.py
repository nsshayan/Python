from subprocess import Popen

#p = Popen("ls -l | wc -l", shell=True)
p = Popen(["ls", "-l", ">", "ls.out"], shell=True)

print("Lauched ls command...")
ret = p.wait()
print("ls complete: exit code:", ret)
