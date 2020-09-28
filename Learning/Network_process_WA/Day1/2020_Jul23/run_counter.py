from subprocess import Popen, PIPE
with Popen("./counter.py", bufsize=65536, stdout=PIPE, encoding="utf8") as p:
    while True:
        ch = p.stdout.read(1)
        if not ch: break
        print(ch, end="")
        