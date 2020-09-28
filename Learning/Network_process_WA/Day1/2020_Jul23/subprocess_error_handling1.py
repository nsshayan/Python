from subprocess import Popen, STDOUT

with open("ls.out", "w") as outfile:
    ret = Popen(["ls", "-l", "/khk", "/usr"], stderr=STDOUT, stdout=outfile).wait()
    print("command completed: ret =", ret)
