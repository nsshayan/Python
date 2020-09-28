from subprocess import Popen
import readline
from shlex import split

while True:
    command = input("PyShell> ")
    ret = Popen(split(command)).wait()
    print("Ret =", ret)
