from subprocess import Popen

with open("ls_new.out", "w") as outfile:
    p = Popen(["ls", "-l"], stdout=outfile)
    ret = p.wait()
    print("ls command returned", ret)

