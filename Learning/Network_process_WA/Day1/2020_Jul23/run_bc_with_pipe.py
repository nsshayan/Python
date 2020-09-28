from subprocess import Popen, PIPE

commands = b"""
scale=2000
4*a(1)
quit
"""

calc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)
calc.stdin.write(commands)
calc.stdin.close()

for line in calc.stdout:
    print(line)
