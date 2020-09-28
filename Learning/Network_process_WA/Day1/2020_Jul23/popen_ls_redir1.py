from subprocess import Popen, STDOUT

with open("lsoutput.txt", "wb") as outfile, \
        open("lserrors.txt", "wb") as errfile:
    p = Popen(["ls", "-l", "/", "/dfsfd"], stdout=outfile, stderr=STDOUT)
    p.wait()
