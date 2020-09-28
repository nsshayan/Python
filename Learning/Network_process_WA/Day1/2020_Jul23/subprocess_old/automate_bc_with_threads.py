from subprocess import PIPE, Popen
from time import time
from threading import Thread

def send_command(out):
    while True:
        command = input("bc> ")
        out.write(bytes(command + "\n", "utf8"))
        out.flush()

def get_output(instream):
    for line in instream:
        print("OUT:" + str(line, "utf8"))


bc = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

input_thread = Thread(target=send_command, args=(bc.stdin,))
output_thread = Thread(target=get_output, args=(bc.stdout,))

input_thread.start()
output_thread.start()

input_thread.join()
output_thread.join()


