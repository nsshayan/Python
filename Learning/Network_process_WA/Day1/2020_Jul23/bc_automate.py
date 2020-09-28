from subprocess import Popen, PIPE

with Popen("bc", stdin=PIPE, stdout=PIPE, encoding="utf8") as calc:
    while True:
        command = input("calc> ")
        calc.stdin.write(command + "\n")
        calc.stdin.flush()

        for line in calc.stdout:
            print(line)
