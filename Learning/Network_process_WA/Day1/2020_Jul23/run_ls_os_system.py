from subprocess import Popen

ret = Popen("ls | wc -l", shell=True).wait()
print("*** ls exited with exit code =", ret)
