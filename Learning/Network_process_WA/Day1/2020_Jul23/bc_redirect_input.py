from subprocess import Popen

with open("bc_commands.txt", "r") as infile, \
     open("bc_output.log", "w") as outfile, \
     open("bc_errors.log", "w") as errfile:
    p = Popen(["bc", "-l"], stdin=infile, stdout=outfile, stderr=errfile)
    p.wait()

