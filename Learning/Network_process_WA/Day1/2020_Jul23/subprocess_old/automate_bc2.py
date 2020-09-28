from subprocess import PIPE, Popen
from sys import stdout, stdin
from multiprocessing import Process

def send_data(p):
    from sys import stdin
    while True:
        print("bc>", end=' ')
        data = stdin.read()
        p.stdin.write(data)
        p.stdin.flush()


def recv_data(p):
    while True:
        for line in p.stdout:
            print(line, end=' ')
            stdout.flush()

cmd = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)
print("BC started... connecting...")

s = Process(target=send_data, args=(cmd,))
r = Process(target=recv_data, args=(cmd,))

s.start()
r.start()

cmd.wait()

