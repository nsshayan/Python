
#### thread_pool_exercise.py #####
"""
Implement 'thread_pool' module hosting 'ThreadPool'
class that allows us to create a pool of worker threads
waiting on a job-queue for any jobs (functions) to be
submitted.

Implement the ThreadPool class such that the code within
the '__main__' namespace works.

"""
from thread_pool import ThreadPool
from time import sleep

if __name__ == '__main__':

    def foo(x, y):
        print("foo called: x = {}, y = {}".format(x, y))
        sleep(4)
        return "foo result", x + y

    def bar(x, y):
        print("bar called: x = {}, y = {}".format(x, y))
        sleep(5)
        return "bar result", x * y

    def test(x):
        print("test called: x = {}".format(x))
        sleep(2)
        return "test result", x ** x

    def square(x):
        from time import sleep
        sleep(0.5)
        return x*x

    #with ThreadPool(workers=10) as pool:
    #    foo_result = pool.submit(fn=foo, args=(10, 20))
    #    bar_result = pool.submit(fn=bar, args=("Hello", 10))
    #    test_result = pool.submit(fn=test, args=(100,))

    results = []

    pool = ThreadPool(workers=10)
    pool.start()
    results.append(pool.submit(fn=foo, args=(10, 20)))
    results.append(pool.submit(fn=bar, args=("Hello", 10)))
    results.append(pool.submit(fn=test, args=(100,)))

    while results:
        for r in results:
            if r.ready:
                print("result = ", r.result)
                results.remove(r)
        sleep(0.5)

    #print(foo_result.result(), bar_result.result(), test_result.result())

    pool.stop()
