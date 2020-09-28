from subprocess import Popen

p = Popen("atom")

from time import sleep
for i in range(5):
    print("Counting", i)
    sleep(1)

p.kill()

    
