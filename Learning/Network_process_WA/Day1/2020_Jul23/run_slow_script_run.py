from subprocess import run, TimeoutExpired
from time import sleep

try: 
    ret = run("./slow_script.sh", timeout=5)
    #for i in range(5):
    #    print("Python program counting: ", i)
    #    sleep(1)
except TimeoutExpired as e:
    print("Timeout occurred!")
else:
    print("./slow_script.sh completed: ret =", ret)
