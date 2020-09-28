from subprocess import Popen, PIPE
from time import time
commands = b"""
scale=2000
4*a(1)
exit
"""

bc_program = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)
start = time()
bc_program.stdin.write(commands)
bc_program.stdin.close()
output = str(bc_program.stdout.read(), "utf8")
end = time()

print("Duration:", end - start)


