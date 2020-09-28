
from subprocess import Popen, PIPE

data = """
bbbbbbb
eeeeeee
aaaaaaa
ddddddd
fffffff
aabbccd
rereere
efefefe
"""

with Popen("sort", stdin=PIPE, stdout=PIPE, encoding="utf8") as p:
    p.stdin.write(data)
    p.stdin.close()
    for line in p.stdout:
        print(line)