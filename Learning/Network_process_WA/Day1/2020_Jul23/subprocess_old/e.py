from subprocess import Popen
from time import sleep

p = Popen("gedit")

sleep(15)

p.kill()
# p.terminate()



