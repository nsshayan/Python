from subprocess import Popen, PIPE
from threading import Thread
import rlcompleter

def input_loop(proc):
    while True:
        command = input("bc> ")
        proc.stdin.write(command + "\n")
        proc.stdin.flush()

def output_loop(proc):
    for line in proc.stdout:
        print(line)

p = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

process_input = Thread(target=input_loop, args=(p,))
process_output = Thread(target=output_loop, args=(p,))

process_input.start()
process_output.start()

process_input.join()
process_output.join()
