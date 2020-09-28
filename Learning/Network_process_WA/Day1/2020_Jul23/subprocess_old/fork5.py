import os
from time import sleep

def child_handler():
   for i in range(30):
       print("In child[%d]: counting %d" % (os.getpid(), i))
   exit(0)

curr_pid = os.getpid()

for i in range(5):
    ret = os.fork()
    if ret == 0: child_handler()

print("Main program exited.")
input("Press enter to quit\n")

        


