from subprocess import Popen, PIPE
from time import time
from threading import Thread, Event
from sys import stdout

stop_thread = Event()

def get_output(stream):
    try:
        while not stop_thread.is_set():
            line = stream.readline()
            stdout.write(line)
    except Exception as e:
        stop_thread.set()


def get_input(stream):
    try:
        while not stop_thread.is_set():
            line = input("calc> ")
            stream.write(line + "\n")
            stream.flush()
    except Exception as e:
        stop_thread.set()

if __name__ == '__main__':
    calc = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

    input_thread = Thread(target=get_input, args=(calc.stdin,))
    output_thread = Thread(target=get_output, args=(calc.stdout,))

    input_thread.start()
    output_thread.start()

    threads = {input_thread, output_thread}

    for t in threads:
        t.join(timeout=2)
        if not t.is_alive(): threads.remove(t)