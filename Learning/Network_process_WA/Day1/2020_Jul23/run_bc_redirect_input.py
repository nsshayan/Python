from subprocess import Popen

with open("sqrt.bc", "rb") as infile, \
     open("bc.output", "wb") as outfile:
    p = Popen("bc", stdin=infile, stdout=outfile)

    ret = p.wait()
