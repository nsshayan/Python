#!/usr/bin/env python
from subprocess import Popen, PIPE
from time import time

calc_pi = b"""
scale=2000
4*a(1)
quit
"""

p = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)
start = time()
p.stdin.write(calc_pi)
p.stdin.flush()
p.wait()
end = time()
print("Duration to calculate PI: %f seconds" % (end - start))
for line in p.stdout:
    print(line)


