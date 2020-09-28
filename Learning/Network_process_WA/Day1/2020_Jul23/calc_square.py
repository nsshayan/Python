from subprocess import Popen, PIPE

commands = """
scale=1000
sqrt(2)
quit
"""

with Popen("bc", stdin=PIPE, stdout=PIPE, encoding="utf8") as p:
    p.stdin.write(commands)
    p.stdin.close()
    
    for line in p.stdout:
        print("OUT:", line)
        