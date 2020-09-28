from subprocess import run, Popen
from time import sleep
import subprocess

#p = Popen("./long_script.sh")
try:
    p = subprocess.run("./long_script.sh", timeout=5)
except subprocess.TimeoutExpired as e:
    print("Program timed out...")
    
#for i in range(5):
#    print("Python program: counting", i)
#    sleep(1)
    
#p.kill()
#p.terminate()

    