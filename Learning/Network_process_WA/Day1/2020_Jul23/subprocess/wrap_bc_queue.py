from subprocess import Popen, PIPE
from threading import Thread
from queue import Queue

import rlcompleter

class HandleIO:
    def __init__(self, proc, prompt="bc> ", bufsize=1000):
        self.proc = proc
        self.prompt = prompt
        self.output = Queue(bufsize)

        self.input_thread = Thread(target=self.handle_input)
        self.output_thread = Thread(target=self.handle_output)
        self.input_thread.start()
        self.output_thread.start()

    def handle_input(self):
        while True:
            if self.output.empty():
                command = input(self.prompt)
                self.proc.stdin.write(command + "\n")
                self.proc.stdin.flush()
            else:
                line = self.output.get()
                if line is None:
                    break
                print(line, flush=True)

    def handle_output(self):
        for line in self.proc.stdout:
            self.output.put(line)
        self.output.put(None)

p = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

HandleIO(p)

