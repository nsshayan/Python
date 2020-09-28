from subprocess import Popen, PIPE, DEVNULL
from time import time

calc_commands = """
scale=3000
4*a(1)
quit
"""

with Popen(["bc", "-l"],
           stdin=PIPE, stdout=DEVNULL,
           encoding="utf8") as proc:
    start = time()
    proc.stdin.write(calc_commands)
    proc.stdin.close()
    proc.wait()
    duration = time() - start

print(f"Calculating value of Pi to 3000 decimal points took {duration} seconds")
