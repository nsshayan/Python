#!/usr/bin/env python

import paramiko

from getpass import getpass

class RingBuffer:
    def __init__(self, capacity=30):
        from collections import deque
        self.buffer = list(range(capacity))
        self.capacity = capacity
        self.cursor = 0

    def put(self, data):
        self.buffer[self.cursor % self.capacity] = data
        self.cursor += 1

    def show(self):
        for data in self.buffer: print(data)

    def __str__(self):
        return "RingBuffer({})".format(str(self.buffer))


class SWBuffer:
    def __init__(self, capacity=30):
        from queue import Queue
        self.queue = Queue(capacity)
        self.capacity = capacity
        self.size = 0

    def put(self, data):
        if self.size >= self.capacity: self.queue.get()
        self.queue.put(data)
        self.size += 1

    def get(self):
        data = self.queue.get()
        self.size -= 1

    def fetch_all(self):
        for i in range(self.size):
            yield self.queue.get()

if __name__ == '__main__':
    t = paramiko.Transport(("192.168.56.101", 22))
    t.connect(username="root", password="welcome")
    sftp = paramiko.SFTPClient.from_transport(t)

    buffer = RingBuffer(5)
    #buffer = SWBuffer(5)

    with sftp.open("/root/system.log", "r") as logfile:
        for line in logfile:
            if "192.168" in line: buffer.put(line)


    #for line in buffer.fetch_all(): print line
    buffer.show()
    t.close()
