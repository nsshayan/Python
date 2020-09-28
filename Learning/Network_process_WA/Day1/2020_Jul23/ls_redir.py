from subprocess import Popen

#ret = Popen(["ls", ">",  "ls.out"]).wait()
with open("ls.out", "wb") as outfile, \
     open("ls.err", "wb") as errfile:
    ret = Popen(["ls", "-l", "/usr", "/opt"], 
                stdout=outfile,
                stderr=errfile).wait()


