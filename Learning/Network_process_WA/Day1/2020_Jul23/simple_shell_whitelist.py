from subprocess import Popen
import rlcompleter
import shlex

commands = "ls", "whoami", "uname"

while True:
    command = input("Cmd> ")
    if "exit" in command:
        break

    if command not in commands:
        print(command, "not allowed")
        continue

    try:
        #        exit_code = Popen(command.split()).wait()
        exit_code = Popen(shlex.split(command)).wait()

        print("exit_code =", exit_code)
    except FileNotFoundError as e:
        print("Invalid command - ", command)
