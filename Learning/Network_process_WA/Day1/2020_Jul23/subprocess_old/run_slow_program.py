from subprocess import Popen, PIPE

p = Popen(["python", "run_loop.py"], bufsize=10, stdout=PIPE)
#p = Popen(["./slow_program.sh"], stdout=PIPE)

#p = Popen(["ls", "-lR", "/"], stdout=PIPE)

for line in p.stdout:
    print(line.upper())

p.wait()

