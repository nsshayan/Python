from subprocess import Popen

#p = Popen('ls')
#print("Created a new process:", p)
#ret = p.wait()

ret = Popen(["ls", "-l",  ">", "ls.out"]).wait()
print("ls command completed: ret =", ret)