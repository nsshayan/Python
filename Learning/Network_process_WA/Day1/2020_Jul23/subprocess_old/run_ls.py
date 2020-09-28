from subprocess import Popen

#p = Popen(["ls", "-l", "/usr", ">", "ls.out"])

#with open("ls.out", "w") as outfile, open("ls.err", "w") as errfile:
with open("ls.out", "a") as outfile:
    #p = Popen(["ls", "-l", "/usr", "/sdfsdf"], stdout=outfile, stderr=errfile)
    p = Popen(["ls", "-l", "/usr", "/sdfsdf"], stdout=outfile, stderr=outfile)
    p.wait()

