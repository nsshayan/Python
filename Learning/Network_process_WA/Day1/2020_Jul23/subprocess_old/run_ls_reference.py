from subprocess import Popen
p = Popen(["ls", "-l", "/usr/sdfsdf"])

#p = Popen("ls -l /usr", shell=True)
#from os import environ
#environ["TESTVAR"] = "Test data"

#p = Popen("echo $TESTVAR", shell=True)
ret = p.wait()
print("Ret = ", ret)


#from os import system
#system("ls -l")

#from os import fork, execve, wait

#pid = fork()
#if pid == 0:
#    execve("ls", ("ls", "-l"), None)
#elif pid > 0:
#    wait()

#pid = fork()
#if pid == 0:
#    execve("/bin/sh", ("/bin/sh", "-c", "ls -l"), None)
#elif pid > 0:
#    wait()


