from subprocess import Popen, STDOUT, DEVNULL

#with open("/dev/null", "w") as outfile:

ret = Popen(["ls", "-l", "/khk", "/usr"], stderr=DEVNULL, stdout=DEVNULL).wait()
print("command completed: ret =", ret)
