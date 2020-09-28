from time import sleep
from sys import stdout

for i in range(10):
    print("Counting:", i)
    stdout.flush()
    sleep(1)

