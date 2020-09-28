from subprocess import Popen, PIPE
from threading import Timer


def timeout(p):
    print("*** Timeout occurred ***")
    p.kill()


with Popen("./run_countloop.sh", stdout=PIPE, encoding="utf8") as p:
    timeout_thread = Timer(interval=5, function=timeout, args=(p,))
    timeout_thread.start()

    for line in p.stdout:
        print(line.upper())
