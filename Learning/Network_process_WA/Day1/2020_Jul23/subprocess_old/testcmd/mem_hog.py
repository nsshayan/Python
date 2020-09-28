#!/usr/bin/env python3
import time
import random
from itertools import count

for c in count(1):
   a = list(range(random.randint(10000, 9000000)))
   time.sleep(random.randint(2,20))
   del a
   print("Count:", c)


