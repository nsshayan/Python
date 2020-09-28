from subprocess import Popen

p = Popen("ls")
print("Started ls command...")
ret = p.wait()
print("ls command complete: return code =", ret)


