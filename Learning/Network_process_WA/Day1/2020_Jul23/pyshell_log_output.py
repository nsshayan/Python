from subprocess import Popen
import rlcompleter
import shlex
from time import ctime

with open("output.log", "a") as logfile:
    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        print(f"======= {ctime()}: running {command} ======== ",
              file=logfile, flush=True)
        ret = Popen(shlex.split(command),
                    stdout=logfile, stderr=logfile
        ).wait()
        print(f"------ {ctime()}: {command} completed --------",
              file=logfile, flush=True)
