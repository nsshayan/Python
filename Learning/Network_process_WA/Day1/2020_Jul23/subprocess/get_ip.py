from subprocess import Popen, PIPE


p = Popen("./slow_script.sh", stdout=PIPE, universal_newlines=True)

for line in p.stdout:
    print(line)

ret = p.wait()
