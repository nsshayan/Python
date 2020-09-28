from subprocess import Popen, PIPE

commands = """
r = 45 + 67
print("result =", r)
print("Hello world from inner python REPL...")
exit()
"""

with Popen("python", encoding="utf8", stdout=PIPE, stdin=PIPE) as p:
    p.stdin.write(commands)
    p.stdin.close()
    for line in p.stdout:
        print(line)
