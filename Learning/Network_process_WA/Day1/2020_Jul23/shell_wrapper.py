from subprocess import Popen
import rlcompleter
import shlex

while True:
    command = input("Shell> ")
    if command == "exit": break
    #exit_code = Popen(command.split()).wait()
    exit_code = Popen(shlex.split(command)).wait()
    print("Exit code: ", exit_code)
