from subprocess import Popen, PIPE

calc = Popen("bc", stdout=PIPE, stdin=PIPE, encoding="utf8")

while True:
    line = input("Enter expression: ")
    if not line: break
    calc.stdin.write(line + "\n")
    calc.stdin.flush()
    for r in calc.stdout:
        print(r)
    #result = calc.stdout.readline()
    #print("Result:", result)

calc.stdin.close()
