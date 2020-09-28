from subprocess import Popen
import rlcompleter
import shlex

exit_code = 0
while True:
    command = input(f"[{exit_code}]Pyshell> ")
    #exit_code = Popen(command, shell=True).wait()
    try:
        #exit_code = Popen(command.split()).wait()
        exit_code = Popen(shlex.split(command)).wait()
    except FileNotFoundError:
        print(f"{command}: not found")
