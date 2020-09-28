from subprocess import Popen

#with open("ls.out", "wb") as outfile, open("ls.err", "wb") as errfile:
#    p = Popen(["ls", "-l", "/usr", "/var", "/etc", "/sdfsdf"],
#              stdout=outfile, stderr=errfile)

with open("ls.out", "ab") as outfile:
    p = Popen(["ls", "-l", "/usr", "/var", "/etc", "/sdfsdf"],
              stdout=outfile, stderr=outfile)

ret = p.wait()
print("ls completed with exitcode =", ret)
