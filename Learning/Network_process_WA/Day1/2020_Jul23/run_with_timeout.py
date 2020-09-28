from subprocess import Popen, TimeoutExpired
from time import sleep

try:
    p = Popen("./slow_script.sh")
    ret = p.wait(5)

except TimeoutExpired as e:
    print("*** Timeout ocurred...")
    #p.kill()


