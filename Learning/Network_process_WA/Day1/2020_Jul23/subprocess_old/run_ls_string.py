from subprocess import Popen, PIPE
p = Popen("ls -lRt | sort | uniq", shell=True)  # sh -c "ls -lRt"
 

p.wait()


