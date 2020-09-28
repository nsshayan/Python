from time import sleep
''' Not a pythonic way. Change it and implement it using the pythonic way '''
""" 
Non-optimized code:
class Tasks:
    def __init__(self):
        self.run_queue = []

    def add(self, fn, *args, **kwargs):
        task = fn(*args, **kwargs)
        self.run_queue.append(task)

    def schedule(self):
        while self.run_queue:
            for task in self.run_queue:
                try:
                    next(task)
                except StopIteration:
                    self.run_queue.remove(task)
 """
#  Optimized Code
class Tasks:
    def __init__(self):
        from collections import deque
        self.run_queue = deque()

    def add(self, fn, *args, **kwargs):
        task = fn(*args, **kwargs)
        self.run_queue.append(task)

    def schedule(self):
        while self.run_queue:
            task=self.run_queue[0]
            try:
                next(task)
            except StopIteration:
                self.run_queue.popleft()
            else:
                self.run_queue.rotate(-1)

#Co-operative multitasking - There are side effect [N:1 threading model] bunch of routines should be used when you need I/O intensive tasks
def foo():
    for i in range(10):
        print("foo(): counting", i)
        yield
        sleep(1)

def bar():
    for i in range(10):
        print("bar(): counting", i)
        yield
        sleep(1)

if __name__ == '__main__':
    tasks = Tasks()
    tasks.add(foo)
    tasks.add(bar)
    tasks.schedule()
