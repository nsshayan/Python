from subprocess import Popen, PIPE
from threading import Thread


def process_input(proc):
    while True:
        line = input("Enter expression: ")
        if not line: break
        proc.stdin.write(line + "\n")
        #calc.stdin.flush()
    proc.stdin.close()
    
def process_output(proc):
    for line in proc.stdout:
        print(">>>", line)

if __name__ == '__main__':
    calc = Popen("bc", stdout=PIPE, stdin=PIPE, encoding="utf8", bufsize=0)
    inthread = Thread(target=process_input, args=(calc,))
    outthread = Thread(target=process_output, args=(calc,))
    inthread.start()
    outthread.start()
    
    inthread.join()
    
    