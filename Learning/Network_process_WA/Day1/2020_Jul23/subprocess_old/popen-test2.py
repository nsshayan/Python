from subprocess import Popen
from time import sleep

p = Popen("./loop.py")

for i in range(15):
    print("In main program, i = ", i)
    sleep(1)

p.wait()
print("Child process exited.")


