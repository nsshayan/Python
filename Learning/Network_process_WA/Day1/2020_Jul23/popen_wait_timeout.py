from subprocess import Popen, TimeoutExpired
from time import sleep
import signal

p = Popen("./simple_loop.sh")
print(f"{p.args} launched: ")
try:
    p.wait(5)
except TimeoutExpired:
    p.terminate()
