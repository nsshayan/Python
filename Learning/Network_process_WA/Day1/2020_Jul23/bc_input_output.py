from subprocess import Popen

with open("bc.input", "r") as infile, open("bc.output", "w") as outfile:
    p = Popen("bc", stdin=infile, stdout=outfile)
    ret = p.wait()
    print("bc command returned", ret)

