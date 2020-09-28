import gevent
from gevent import monkey
monkey.patch_all()

from subprocess import PIPE, Popen
from time import time

def send_command(out):
    while True:
        command = input("bc> ")
        out.write(command + "\n")
        out.flush()
#        gevent.sleep(0)

def get_output(instream):
    for line in instream:
        #print("OUT:" + str(line, "utf8"))
        print(line)
#        gevent.sleep(0)

bc = Popen(["bc", "-li"], stdout=PIPE, stdin=PIPE, encoding="utf8")


input_greenlet = gevent.spawn(send_command, bc.stdin)
output_greenlet = gevent.spawn(get_output, bc.stdout)

gevent.joinall([input_greenlet, output_greenlet])


