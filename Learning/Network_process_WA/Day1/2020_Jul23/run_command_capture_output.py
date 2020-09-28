from subprocess import Popen

with open("command.out", "wb") as outfile:
    Popen(["uname", "-a"], stdout=outfile).wait()
    
with open("fruits.txt", "rb") as infile, \
     open("output.txt", "wb") as outfile:
    Popen("sort", stdin=infile, stdout=outfile).wait()
    