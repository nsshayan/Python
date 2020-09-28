from subprocess import Popen, TimeoutExpired
from time import sleep
from sys import argv

p = Popen("./slow_script.sh")
print("Process launched: p =", p)
for i in range(5):
    print(f"{argv[0]} running...")
    sleep(1)

# p.terminate()
#exit_code = p.wait()

try:
    exit_code = p.wait(2)
except TimeoutExpired as e:
    print("Child process timed out")
    p.kill()

#print("Process exited: exit_code =", exit_code)
