from subprocess import Popen
from time import sleep

child = Popen("./loop.sh")
print("Launched ./loop.sh with pid =", child.pid)
for i in range(5):
    print("In python: counting", i)
    sleep(1)

print("Waiting for child to complete...")
ret = child.wait()
print("Child completed: exit code =", ret)


# https://public.etherpad-mozilla.org/p/Advanced_Python
