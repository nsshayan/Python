from subprocess import Popen


with open("sqrt.bc", "rb") as infile:
    p = Popen("bc", stdin=infile)

ret = p.wait()
print("bc completed with exitcode =", ret)
