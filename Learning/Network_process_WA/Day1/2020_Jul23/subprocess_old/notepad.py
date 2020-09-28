from subprocess import Popen, PIPE
from time import sleep

p = Popen(args="notepad")

sleep(5)

print("Terminating notepad...")
p.kill()


