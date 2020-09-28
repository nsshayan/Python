from subprocess import Popen, PIPE
from threading import Thread


def send_input(proc):
    while True:
        command = input("calc> ")
        if command == "exit":
            break

        proc.stdin.write(command + "\n")


def get_output(proc):
    for line in proc.stdout:
        print(line.strip())


with Popen("bc", stdout=PIPE, stdin=PIPE, bufsize=0, encoding="utf8") as calc:
    input_thread = Thread(target=send_input, args=(calc,))
    output_thread = Thread(target=get_output, args=(calc,))

    input_thread.start()
    output_thread.start()

    input_thread.join()
