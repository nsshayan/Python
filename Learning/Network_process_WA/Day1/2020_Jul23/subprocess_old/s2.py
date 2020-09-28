from subprocess import Popen, PIPE
from time import sleep

#p = Popen("ls slkjfsdf", stdout=PIPE, stderr=PIPE, shell=True)
p = Popen(["ls", "-l"], stdout=PIPE, stderr=PIPE)
print("Program started... waiting for it to exit")

print(p.stdout.read().upper())


ret = p.wait()
print("Program finished, exit code = ", ret)

#sleep(10)
#p.kill()

