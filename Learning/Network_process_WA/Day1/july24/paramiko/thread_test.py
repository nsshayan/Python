from gevent import monkey; monkey.patch_all()

from threading import Thread, current_thread

def foo():
    t = current_thread()
    print("Running", t.name)
    from time import sleep
    sleep(60)

if __name__ == '__main__':
    for i in range(1000000):
        Thread(target=foo).start()

