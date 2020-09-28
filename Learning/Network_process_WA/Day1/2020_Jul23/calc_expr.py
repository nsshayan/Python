from subprocess import Popen

with open("expressions.input", "rb") as infile, \
        open("expressions.output", "wb") as outfile:
    p = Popen("bc", stdin=infile, stdout=outfile)
    p.wait()
