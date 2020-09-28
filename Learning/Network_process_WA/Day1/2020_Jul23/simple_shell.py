from subprocess import Popen
import rlcompleter
import shlex

while True:
    command = input("PyShell> ")
    if command == "exit":
        break

    args = shlex.split(command)

    exit_code = Popen(args).wait()
    print("=>", exit_code)
