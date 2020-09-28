#!/usr/bin/env python

import os

pid = os.fork() 

if pid == 0: # child
    os.execv('/usr/bin/python', 
        ['/usr/bin/python', '/Users/posman/Source/Python/wastetime.py'])
elif pid == -1: # error
    print("An error occured")
else:
    print("Parent process id:", os.getpid())
    print("Child process id:", pid)
    status = os.waitpid(pid, 0)
    print(status)
