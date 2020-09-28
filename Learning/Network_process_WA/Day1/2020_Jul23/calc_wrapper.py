from subprocess import Popen, PIPE
from time import time

calc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

while True:
    command = input("calc> ")
    calc.stdin.write(command)
    calc.stdin.flush()

    for line in calc.stdout:
        print(line)
