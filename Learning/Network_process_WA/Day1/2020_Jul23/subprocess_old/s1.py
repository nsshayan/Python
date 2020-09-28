from subprocess import Popen
from time import sleep

p = Popen("gedit")
print("Program started... waiting for it to exit")
p.wait()
print("Program finished, back to python...")

#sleep(10)
#p.kill()

