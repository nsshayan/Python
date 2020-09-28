from subprocess import Popen

with open("bc.in") as infile:
    p = Popen("bc", stdin=infile)
    p.wait()



