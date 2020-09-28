from subprocess import Popen, PIPE
from collections import deque


p = Popen(["ls", "-lR", "/usr/local/lib"], stdout=PIPE, universal_newlines=True)

#for line in p.stdout:
#    if "inet " in line:
#        print(line.split()[1])

#lines = p.stdout.readlines()
#print(lines[-5:])

class RingBuffer:
    def __init__(self, size):
        self.queue = deque()
        self.size = size
        self.index = 0

    def push(self, data):
        self.queue.append(data)
        self.index += 1
        if self.index >= self.size:
            self.queue.popleft()

    def __str__(self):
        return "".join(self.queue)

queue = RingBuffer(5)

for line in p.stdout:
    queue.push(line)

print(queue)
ret = p.wait()
