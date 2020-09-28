from subprocess import Popen, STDOUT, DEVNULL

# with open("lsoutput.txt", "wb") as outfile, \
#        open("lserrors.txt", "wb") as errfile:

# with open("NUL", "wb") as outfile:
# with open("/dev/null", "wb") as outfile:
#    p = Popen(["ls", "-l", "/", "/dfsfd"], stdout=outfile, stderr=outfile)
#    p.wait()

p = Popen(["ls", "-l", "/", "/dfsfd"], stdout=DEVNULL, stderr=DEVNULL)
r = p.wait()
print(r)
