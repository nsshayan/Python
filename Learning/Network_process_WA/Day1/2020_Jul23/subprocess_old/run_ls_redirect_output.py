from subprocess import Popen

with open("ls.out", "w") as out:
    p = Popen(["ls",  "/bin", "/usr"], stdout=out)
    print("Started ls command...")
    ret = p.wait()
    print("ls command finished, ret =", ret)
