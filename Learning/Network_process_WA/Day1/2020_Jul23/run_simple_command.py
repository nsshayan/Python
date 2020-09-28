from subprocess import Popen
from time import sleep

p = Popen("./simple_script.sh")
for i in range(5):
    print(f"Python program counting {i}")
    sleep(1)

print("Waiting for script to complete...")
ret = p.wait()
print(f"Script completed: ret = {ret}")
