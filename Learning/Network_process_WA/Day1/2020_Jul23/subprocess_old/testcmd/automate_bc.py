from subprocess import Popen, PIPE
from time import time


bc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)

while True:
    command = raw_input("Enter command: ")
    bc.stdin.write(command.strip())
    for line in bc.stdout:
        print line





