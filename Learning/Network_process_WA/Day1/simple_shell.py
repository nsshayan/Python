from subprocess import Popen
import rlcompleter
# all the command line editing.
while True:
    command = input("PyShell> ")
    if command == "exit":
        break
    exit_code = Popen(command).wait()
    print("=>", exit_code)