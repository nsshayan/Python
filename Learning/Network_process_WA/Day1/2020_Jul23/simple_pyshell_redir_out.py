from subprocess import Popen
import rlcompleter
import shlex

exit_code = 0
while True:
    command = input(f"[{exit_code}]Pyshell> ")
    try:
        args = shlex.split(command)
        with open(f"{args[0]}.out", "w") as outfile:
            exit_code = Popen(args, stdout=outfile, stderr=errfile).wait()
    except FileNotFoundError:
        print(f"{command}: not found")
