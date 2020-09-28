from subprocess import Popen, TimeoutExpired
import os
from shlex import split, quote
import rlcompleter

command = "mkdir "

while True:
    dirname = input("Enter directory to create: ")
    if not dirname:
        break
    #child = Popen(command + dirname, shell=True)
    child = Popen(command + quote(dirname), shell=True)
    ret = child.wait()
    print("Exit code: ", ret)
