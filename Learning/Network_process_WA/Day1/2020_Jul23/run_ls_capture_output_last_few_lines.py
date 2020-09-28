from subprocess import Popen, PIPE

class RingBuffer:
    def __init__(self, capacity=5):
        self.ring = [None] * capacity
        self.capacity = capacity
        self.i = 0

    def write(self, data):
        # Dont try this in python
        #self.ring[i % self.capacity] = data

        self.ring[self.i] = data
        self.i += 1
        if self.i >= self.capacity:
            self.i = 0

    def __str__(self):
        return "".join(self.ring)


child = Popen(["ls", "-l"], stdout=PIPE, universal_newlines=True)

buffer = RingBuffer(5)
for line in child.stdout:
    buffer.write(line)

print(buffer)


