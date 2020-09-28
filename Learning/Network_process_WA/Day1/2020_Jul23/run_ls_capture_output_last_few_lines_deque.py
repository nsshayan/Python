from subprocess import Popen, PIPE

class RingBuffer:
    def __init__(self, capacity=5):
        from collections import deque
        self.ring = deque
        self.capacity = capacity
        self.i = 0

    def write(self, data):
        self.ring.append(data)
        self.i += 1
        if self.i >= self.capacity:
            self.ring.popleft()


    def __str__(self):
        return "".join(self.ring)


child = Popen(["ls", "-l"], stdout=PIPE, universal_newlines=True)

buffer = RingBuffer(5)
for line in child.stdout:
    buffer.write(line)

print(buffer)


