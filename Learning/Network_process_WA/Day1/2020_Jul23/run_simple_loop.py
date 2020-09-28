from subprocess import Popen
from time import sleep

p = Popen("./simple_loop.sh")
print("Launched the shell script: p =", p)

for i in range(5):
    print("Python program: counting", i)
    sleep(1)
 
p.terminate()   
#p.wait()
#print("The shell script is complete.")
    
