#import subprocess
from subprocess import Popen
from time import sleep

p = Popen("./slow_script.sh")
print("slow_script launched: pid = ", p.pid)
sleep(3)
p.kill()

print(p.returncode)

#for i in range(10):
#    print("Python program running...")
#    sleep(1)

