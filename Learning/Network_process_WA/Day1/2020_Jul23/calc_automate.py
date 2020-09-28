from subprocess import Popen, PIPE

commands = """
scale=1000
sqrt(2)
quit
"""

with Popen("bc", stdin=PIPE, stdout=PIPE, encoding="utf8") as calc:
    calc.stdin.write(commands)
    calc.stdin.close()
    #calc.stdin.flush()

    for line in calc.stdout:
        print(line)
