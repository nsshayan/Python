from subprocess import Popen, PIPE

with Popen("./add.py", stdin=PIPE, stdout=PIPE, encoding="utf8") as proc:
    prompt = proc.stdout.read()
    print(prompt)
    proc.stdin.write("10\n")
    proc.stdin.write("20\n")
    proc.stdin.close()
