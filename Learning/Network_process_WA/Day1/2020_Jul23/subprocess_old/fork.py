#!/usr/bin/env python

import os
import time

count = 0
ret = os.fork() 
if ret == 0: # child
    while True:
        print("In child (%d): %d" % (os.getpid(), count))
        count += 1
        time.sleep(1)
elif ret > 0: # parent
    while True:
        print("In parent (%d): %d" % (os.getpid(), count))
        count += 1
        time.sleep(1)
else:
    print("Failed to fork child...")


