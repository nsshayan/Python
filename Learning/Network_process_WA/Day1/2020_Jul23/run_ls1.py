from subprocess import Popen

p = Popen("./slow_script.sh")
print("python: slow_script.sh launched: p =", p)

ret = p.wait()
print("python: slow_script.sh completed with exit code: ", ret)
