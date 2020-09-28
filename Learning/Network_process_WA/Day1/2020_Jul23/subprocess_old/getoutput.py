from subprocess import Popen, PIPE
from time import sleep

with open("output.txt", "w") as out:
    child = Popen("ls", stdout=out)
    child.wait()
    




