from subprocess import Popen, PIPE
from time import time

commands = """
scale=2000
4 * a(1)
quit
"""

p = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

start = time()
with p.stdin: p.stdin.write(commands)
with p.stdout: contents = p.stdout.read()

end = time()
print("Duration: ", end - start, "seconds")

