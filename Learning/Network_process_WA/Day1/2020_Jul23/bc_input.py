from subprocess import Popen

with open("bc.input", "rb") as infile:
    ret = Popen("bc", stdin=infile).wait()
