from os import system
from itertools import count
from time import sleep

system("./loop.py")

for i in count(0):
    print("In main program, i = ", i)
    sleep(1)


