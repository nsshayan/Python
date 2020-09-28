from subprocess import Popen

with open("ls.out", "wb") as outfile:
    child = Popen(["ls", "-l"], stdout=outfile)
    child.wait()

