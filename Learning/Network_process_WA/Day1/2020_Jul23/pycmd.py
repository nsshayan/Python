from subprocess import Popen
import rlcompleter
import shlex

while True:
    command = input("PyCmd> ")
    if command == "exit": 
        break
    #ret = Popen(command.split()).wait()
    #ret = Popen(shlex.split(command)).wait()
    ret = Popen(command, shell=True).wait()
    print("ret = ", ret)    

