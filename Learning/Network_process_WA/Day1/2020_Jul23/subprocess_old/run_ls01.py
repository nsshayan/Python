from subprocess import Popen

#p = Popen("echo $PATH", shell=True)
with open("ls.out", "w") as lsout:
    p = Popen(["ls", "-l", "/usr"], stdout=lsout)
    ret = p.wait()
    print("ls exited with code =", ret)




