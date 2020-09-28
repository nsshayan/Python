from subprocess import Popen, PIPE
from time import time
from sys import stdin

start_commands = """
scale=2000
sqrt(2)
"""

bc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)
bc.stdin.write(start_commands)
output, error = bc.communicate()
print output
print error






