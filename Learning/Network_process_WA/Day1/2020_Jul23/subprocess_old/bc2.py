from subprocess import Popen, PIPE
from threading import Thread
import sys

def handle_process_input(f):
    while True:
        line = sys.stdin.readline()
        if not line: break
        f.write(line)

def handle_process_output(f):
    while True:
        line = f.readline()
        if not line: break
        sys.stdout.write("Output = " + line)

p = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

i = Thread(target=handle_process_input, args=(p.stdin,))
o = Thread(target=handle_process_output, args=(p.stdout,))

i.start()
o.start()

p.wait()

