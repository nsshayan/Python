from car import Car
from pickle import dumps
import sys

c1 = Car("Honda", "John")
c2 = Car("Toyota", "Sam")

info = dict(
        name="James",
        city="Mumbai",
        role="Admin",
        depts=["IT", "Support", "Admin"]
)

data = dumps(c1)
#data += dumps(c2)
#data += dumps(info)

sys.stdout.write(data)

        


