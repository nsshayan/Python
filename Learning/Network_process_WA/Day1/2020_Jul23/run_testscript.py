from subprocess import Popen
from time import sleep

#p = Popen("./testscript.py sdfsd")
p = Popen(["./testscript.py", "dsfdf"])

for i in range(5):
    print("Counting", i)
    sleep(1)

#p.wait()
p.kill()

print("./testscript.py complete...")