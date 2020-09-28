#import subprocess
from subprocess import Popen
from time import sleep

p = Popen("./slow_script.sh")
ret = p.wait()
for i in range(10):
    print("Python program running...")
    sleep(1)

