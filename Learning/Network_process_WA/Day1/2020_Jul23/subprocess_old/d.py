from subprocess import Popen, PIPE
from time import sleep
import sys

p = Popen("./wait.sh")

p.wait()

print("Back to python program...")
for i in range(10):
    sleep(1)
    print(".", end=' ')
    sys.stdout.flush()

