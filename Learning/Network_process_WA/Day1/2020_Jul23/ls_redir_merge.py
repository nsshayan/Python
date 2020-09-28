from subprocess import Popen, STDOUT

with open("ls.out", "wb") as outfile:
    ret = Popen(["ls", "-l", "/usr", "/opt"], 
                stdout=outfile,
                stderr=STDOUT).wait()


