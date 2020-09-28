from subprocess import Popen

# with open("NUL", "w") as nullfile
with open("/dev/null", "w") as nullfile:
    p = Popen("ls", stdout=nullfile)
    p.wait()
