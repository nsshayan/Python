from subprocess import Popen
import rlcompleter
import shlex

while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    #ret = Popen(command.split()).wait()
    ret = Popen(shlex.split(command)).wait()
    print("Exit code: ", ret)
