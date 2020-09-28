from subprocess import PIPE, Popen
from sys import stdout
from threading import Thread

def send_data(p):
    while True:
        data = input("bc> ")
        p.stdin.write(data + "\n")
        p.stdin.flush()


def recv_data(p):
    for line in p.stdout:
        print(line, end=' ')
        stdout.flush()

cmd = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)
print("BC started... connecting...")

s = Thread(target=send_data, args=(cmd,))
r = Thread(target=recv_data, args=(cmd,))

s.start()
r.start()

cmd.wait()

