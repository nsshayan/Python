from gevent import monkey
monkey.patch_all()

from threading import Thread
from time import sleep
from itertools import count


def foo():
    print("In foo...")
    sleep(60)


for i in count():
    print("Creating {} thread".format(i))
    Thread(target=foo).start()
