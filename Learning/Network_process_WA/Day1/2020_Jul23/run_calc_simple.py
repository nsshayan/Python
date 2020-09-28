from subprocess import Popen, PIPE

commands = """
scale=1000
sqrt(2)
quit
"""

calc = Popen("bc", stdout=PIPE, stdin=PIPE, encoding="utf8")
calc.stdin.write(commands)
calc.stdin.close()

for line in calc.stdout:
    print(line)
