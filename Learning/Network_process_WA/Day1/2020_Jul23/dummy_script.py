#!/usr/bin/env python
from random import randint
from itertools import count
from time import sleep, ctime

for _ in range(5):
    print(f"{ctime()}: Generated {randint(1, 1000)}", flush=True)
    sleep(randint(1, 3))
