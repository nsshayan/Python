from subprocess import Popen
from time import sleep
import signal


with Popen("./simple_loop.sh") as p:
    for i in range(5):
        print("counting", i)
        sleep(1)
    p.terminate()
    
p = Popen("./simple_loop.sh")
print(f"{p.args} launched: ")
for i in range(5):
    print("Python program counting", i)
    sleep(1)

#ret = p.wait()
#print("script exited: returned", ret)
#p.kill()
#print("script was killed...")
#p.send_signal(signal.SIGTERM)

p.terminate()
p.send_signal(signal.SIGSTOP)
sleep(2)
p.send_signal(signal.SIGCONT)
