#!/usr/bin/env python
from time import sleep
import os
print(os.getpid())

a = []
for i in range(1000):
    a.append(list(range(100000)))
    sleep(2)

