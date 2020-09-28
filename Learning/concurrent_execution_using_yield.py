from time import sleep

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
    t1 = foo()
    t2 = bar()
    tasks = [t1, t2]
    while tasks:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)

