from time import sleep
from threading import Thread, current_thread
from random import randint

def joinall(threads, interval):
    from collections import deque
    threads = deque(threads)
    while threads:
        t = threads[0]
        t.join(interval)
        if not t.is_alive():
            yield threads.popleft()
        else:
            threads.rotate(-1)



def fn(count):
    th = current_thread()
    for i in range(count):
        print("In {} counting {}/{}".format(th.name, i, count))
        sleep(0.5)  

if __name__ == '__main__':
    threads = []
    for i in range(1, 6):
        t = Thread(target=fn, args=(randint(3, 25),))
        threads.append(t)
        t.start()

    # TODO: Implement this function.
    # First argument should be collection
    # of threads, second argument must
    # be tick interval

    joinall(threads, 0.5)

    print("main complete")
