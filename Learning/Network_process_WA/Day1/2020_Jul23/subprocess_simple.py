from subprocess import Popen
import rlcompleter
import shlex

while True:
    c = input("Shell> ")
    exit_code = Popen(shlex.split(c)).wait()
    print("Exit code =", exit_code)
