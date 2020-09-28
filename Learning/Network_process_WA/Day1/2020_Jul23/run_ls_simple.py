from subprocess import Popen

p = Popen("ls")
print("ls command launched: p =", p)

ret = p.wait()
print("ls command completed: ret =", ret)
