from subprocess import Popen
import shlex
import rlcompleter

while True:
    command = input("Shell> ")
    if command == "exit":
        break
    #ret = Popen(command, shell=True).wait()
    #ret = Popen(command.split()).wait()
    with Popen(shlex.split(command)) as p:
        print("Exit code =", p.wait())
