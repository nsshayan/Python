from subprocess import Popen, run
from time import sleep

#p1 = Popen("./slow_script.sh", )
#p2 = Popen("./slow_script.sh")

p1 = run("./slow_script.sh", timeout=5)

for i in range(5):
    print("Counting", i)
    sleep(1)

#print("waiting for p1 to exit")
#exit_code = p1.wait()
#print("p1 exited with exit code =", exit_code)

#print("waiting for p2 to exit")
#exit_code = p2.wait()
#print("p2 exited with exit code =", exit_code)

#p1.kill()
#p2.kill()
#p1.wait(timeout=5)
#p2.wait(7)

print("main program exiting....")