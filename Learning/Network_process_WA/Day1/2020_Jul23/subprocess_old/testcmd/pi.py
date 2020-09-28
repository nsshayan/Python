from subprocess import Popen, PIPE
from time import time

bc_commands = """
scale=2000
4*a(1)
quit
"""

bc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)
start = time()
bc.stdin.write(bc_commands)
bc.wait()
end = time()

print("Duration: {} seconds".format(end - start))


