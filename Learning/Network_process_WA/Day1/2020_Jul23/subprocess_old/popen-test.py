from subprocess import Popen
from itertools import count
from time import sleep

def system(args):
    p = Popen(args, shell=True)
    return p.wait()


system("./loop.py")

for i in count(0):
    print("In main program, i = ", i)
    sleep(1)


