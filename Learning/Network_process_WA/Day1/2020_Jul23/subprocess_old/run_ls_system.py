from subprocess import Popen

# Emulate os.system()
ret = Popen("ls /bin  /sdfdsf", shell=True).wait()
print("ls command finished, ret =", ret)
