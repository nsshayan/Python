from subprocess import Popen
import os
from time import sleep

#os.system("./slow_script.sh")
p = Popen("./slow_script.sh")
print("back into python program: p =", p)
for i in range(10):
    print(f"Counting {i} in python program")
    sleep(0.5)
ret = p.wait()
print("script exited: ret =", ret)
