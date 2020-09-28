from subprocess import Popen, PIPE

p = Popen("./print_dots.py", stdout=PIPE, encoding="utf8", bufsize=65536)

#for line in p.stdout:
#    print(line)

while not p.stdout.closed:
    c = p.stdout.read(1)
    print(c, end="", flush=True)



#while True:
    #if p.stdout.closed: break
    #c = p.stdout.read(1)
    #print(c, end="", flush=True)
