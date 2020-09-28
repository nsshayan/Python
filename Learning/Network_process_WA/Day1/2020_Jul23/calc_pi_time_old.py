from subprocess import Popen
from time import time

with open("bc_commands.txt") as infile, open("/dev/null", "w") as outfile:
    start = time()
    Popen(["bc", "-l"], stdin=infile, stdout=outfile).wait()
    duration = time() - start

print(f"Took {duration} seconds")