from subprocess import Popen
p = Popen("vim")

data = input("Enter a line: ")




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


