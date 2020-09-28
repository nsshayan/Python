from subprocess import Popen

#ret = Popen("ls /bin", shell=True).wait()
# ret = os.system("ls /bin")

p = Popen("ls")
print("Launched ls command: p =", p, "Pid =", p.pid)

ret = p.wait()
print("ls exited with ret =", ret)