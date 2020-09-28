from subprocess import Popen
with open("output.txt", "w") as out:
    p = Popen(["ls", "-l"], stdout=out)
    ret = p.wait()


