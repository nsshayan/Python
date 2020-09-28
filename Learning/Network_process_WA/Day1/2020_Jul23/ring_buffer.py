class RingBuffer:

    def __init__(self, size, data=[]):
        from collections import deque
        self.__size = size
        if len(data) > size:
            self.__buffer = deque(data[-size:])
        else:
            self.__buffer = deque(data)
        self.__cursor = len(self.__buffer)

    def append(self, data):
        self.__buffer.append(data)
        if self.__cursor < self.__size:
            self.__cursor += 1
        else:
            self.__buffer.popleft()

    def pop(self):
        if self.__cursor > 0:
            self.__cursor -= 1
            return self.__buffer.popleft()
        else:
            raise IndexError("pop from empty buffer")

    def __len__(self):
        return len(self.__buffer)

    def size(self):
        return self.__size

    def __str__(self):
        return f"RingBuffer({self.__size}, [{', '.join([ str(v) for v in self.__buffer])}])"

    __repr__ = __str__

    def __iter__(self):
        return iter(self.__buffer)
