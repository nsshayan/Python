import os
from time import sleep

def foo():
   for i in range(10):
       print("In foo: counting", i)
       sleep(1)


def bar():
   for i in range(10):
       print("In bar: counting", i)
       sleep(1)


ret = os.fork()
if ret > 0:   # In parent
    foo()
elif ret == 0: # In child
    bar()


        


