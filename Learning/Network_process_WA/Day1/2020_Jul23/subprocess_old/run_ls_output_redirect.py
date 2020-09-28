from subprocess import Popen
with open("ls.out", "w") as out:
    p = Popen(["ls", "-l", "/usr"], stdout=out)
ret = p.wait()


