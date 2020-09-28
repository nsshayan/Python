import gevent
from gevent import monkey
monkey.patch_all()

from subprocess import PIPE, Popen
from time import time
from threading import Thread

def send_command(out):
    while True:
        command = input("bc> ")
        out.write(bytes(command + "\n", "utf8"))
        out.flush()
        gevent.sleep(0)

def get_output(instream):
    for line in instream:
        print("OUT:" + str(line, "utf8"))
        gevent.sleep(0)

bc = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

input_greenlet = gevent.spawn(send_command, bc.stdin)
output_greenlet = gevent.spawn(get_output, bc.stdout)

gevent.joinall([input_greenlet, output_greenlet])


