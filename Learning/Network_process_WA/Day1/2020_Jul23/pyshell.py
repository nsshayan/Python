from subprocess import Popen, TimeoutExpired
import os
from shlex import split
import rlcompleter

while True:
    command = input(f"[{os.getpid()}]PyShell> ")
    if command == "exit":
        break
    #child = Popen(command, shell=True)
    #child = Popen(command.split())
    child = Popen(split(command))
    print("Child pid = ", child.pid)

    ret = child.wait()
    print("Exit code: ", ret)
