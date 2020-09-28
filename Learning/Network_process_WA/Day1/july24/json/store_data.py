from car import Car
from pickle import dump

c1 = Car("Honda", "John")
c2 = Car("Toyota", "Sam")

info = dict(
        name="James",
        city="Mumbai",
        role="Admin",
        depts=["IT", "Support", "Admin"]
)

with open("data.dat", "wb") as out:
    dump(c1, out)
    dump(c2, out)
    dump(info, out)

        


