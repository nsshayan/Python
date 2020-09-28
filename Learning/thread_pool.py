from threading import Thread, Event
from queue import Queue

class Future:
    def __init__(self, fn, args, kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.__ready = Event()
        self.__result = None

    def call(self):
        self.__result = self.fn(*self.args, **self.kwargs)
        self.__ready.set()

    @property
    def ready(self):
        return self.__ready.is_set()

    @property
    def result(self):
        self.__ready.wait()
        return self.__result

class ThreadPool:
    def __init__(self, workers, queue_size=None):
        self.workers = []
        qsize = queue_size if queue_size else workers
        self.queue = Queue(qsize)
        self.quit = Event()

        for _ in range(workers):
            thread = Thread(target=self.__wait_on_queue)
            self.workers.append(thread)

    def __wait_on_queue(self):
        while not self.quit.is_set():
            future = self.queue.get()
            if future is None:
                continue
            else:
                future.call()

    def start(self):
        for thread in self.workers:
            thread.start()

    def stop(self):
        self.quit.set()
        for _ in self.workers:
            self.queue.put(None)

    def submit(self, fn, args=(), kwargs={}):
        future = Future(fn, args, kwargs)
        self.queue.put(future)
        return future
