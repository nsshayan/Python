from subprocess import Popen, PIPE, STDOUT, DEVNULL
from time import sleep

#process = Popen(["ls", "-l", "/sdkfsdf", "/"], 
#                stdout=PIPE, stderr=STDOUT, encoding="utf8")

process = Popen("ls", stdout=DEVNULL)
    
for line in process.stdout:
    print(line.upper())
