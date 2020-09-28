#!/usr/bin/python
from time import sleep
from os import getpid

print("Child process id = ", getpid()) 

for i in range(10):
    sleep(1)
    print("Child: counting", i)

