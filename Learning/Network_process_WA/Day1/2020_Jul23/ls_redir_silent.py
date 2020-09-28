from subprocess import Popen, DEVNULL

#ret = Popen(["ls", ">",  "ls.out"]).wait()
#with open("/dev/null", "wb") as outfile:
ret = Popen(["ls", "-l", "/usr", "/opt"], 
                stdout=DEVNULL,
                stderr=DEVNULL).wait()


