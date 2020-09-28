from subprocess import Popen, PIPE
from time import time

commands = """
scale=2000
4*a(1)
quit
"""


p = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

start = time()
p.stdin.write(commands)
p.stdin.close()

#for line in p.stdout:
#    print "-->", line
p.wait()
end = time()
print("Time taken: ", end - start)


