from subprocess import Popen, PIPE
from time import time
from threading import Thread
from sys import stdout


bc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)

def handle_input():
    while True:
        command = raw_input("Enter command: ")
        bc.stdin.write(command + "\n")
        bc.stdin.flush()

def handle_output():
    for line in bc.stdout:
        print "OUT: " + line
        bc.stdout.flush()
        stdout.flush()


input_thread = Thread(target=handle_input)
output_thread = Thread(target=handle_output)

input_thread.start()
output_thread.start()





