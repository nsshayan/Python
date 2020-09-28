from subprocess import Popen, PIPE
from time import time

p = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)

start = time()
p.stdin.write("scale=2000\n")
p.stdin.write("4*a(1)\n")
p.stdin.close()
end = time()

for line in p.stdout:
    print(line)

print("Completed in", (end - start), "seconds")


