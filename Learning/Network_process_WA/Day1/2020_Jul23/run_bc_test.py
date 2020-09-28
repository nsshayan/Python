from subprocess import Popen, PIPE

commands = """
scale=1000
4*a(1)
quit
"""

with Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, encoding="utf8") as calc:
    calc.stdin.write(commands)
    calc.stdin.close()
    for line in calc.stdout:
        print(line)