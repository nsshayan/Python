from subprocess import Popen, PIPE

with Popen("./fast_script.sh", stdout=PIPE, bufsize=1000) as p:
    #for line in p.stdout:
    #    print(line.upper())
    while True:
        data = p.stdout.read(10)
        print(data)
