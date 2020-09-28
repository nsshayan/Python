from subprocess import Popen
from time import sleep

with Popen("./slow_script.sh") as p:
    sleep(2)
    #p.kill()
    p.terminate()
