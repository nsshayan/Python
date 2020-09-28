from subprocess import Popen, TimeoutExpired
import time

p = Popen("./slowscript.sh")

print("./slowscript.sh launched: p =", p.pid)

for i in range(5):
    print("Python program: counting", i)
    time.sleep(1)

try:
    exit_code = p.wait(timeout=5)
except TimeoutExpired as e:
    print("Command did not complete in 5 seconds...")
    #p.kill()
    p.terminate()
else:
    print("shell script completed: exit_code =", exit_code)

print("Python program is complete...")
