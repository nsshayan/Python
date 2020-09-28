from subprocess import PIPE, Popen
from time import time

bc = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

while True:
    command = input("bc> ")
    bc.stdin.write(bytes(command + "\n", "utf8"))
    bc.stdin.flush()

    for line in bc.stdout:
        print("OUT: " + str(line, "utf8"))

