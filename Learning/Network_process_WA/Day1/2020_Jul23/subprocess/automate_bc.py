from subprocess import Popen, PIPE
from time import time
commands = """
scale=2000
4*a(1)
quit
"""
p = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

start = time()
p.stdin.write(commands)
p.stdin.close()
p.wait()
duration = time() - start
print("PI calculation complete in {} seconds.".format(duration))

for line in p.stdout:
    print(line)
