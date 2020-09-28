from subprocess import Popen
from itertools import count
from time import sleep

from os import getpid

print("Process-id = ", getpid())
input()

p = Popen("./fast_script.sh")
#for i in count(1000, 10):
for i in range(10):
   print("Python program: counting", i)
   sleep(2)

print("Program exited...")


