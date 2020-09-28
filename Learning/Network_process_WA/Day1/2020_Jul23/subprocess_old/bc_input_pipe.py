from subprocess import Popen, PIPE

p = Popen(["bc", "-l"], stdin=PIPE)

commands = """
scale=100
4*a(1)
quit
"""

p.stdin.write(commands)
p.stdin.close()
p.wait()

