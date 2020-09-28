from subprocess import Popen
from time import sleep


p = Popen("./slow_script.sh")
print("script launched: p =", p)
print("pid = ", p.pid)

for i in range(5):
    print("Python programming looping: ", i)
    sleep(1)

p.kill()
p.send_signal(2)
print("Child process being force terminated...")