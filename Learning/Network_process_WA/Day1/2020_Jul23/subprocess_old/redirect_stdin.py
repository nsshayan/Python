from subprocess import Popen, PIPE
from time import sleep

with open("in.txt") as input_file:
    child = Popen(["bc", "-l"], stdin=input_file)
    child.wait()
    




