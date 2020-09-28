import shelve
from car import Car


name = "James"

info = {'city' : 'Chennai', 'temperature' : 38, 'country' : 'India' }

scores = [555, 66, 23, 432, 77, 22]

c1 = Car("Honda", "Smith")
c2 = Car("Maruti", "Jones")


with shelve.open("store.dat") as store:
    store['n'] = name
    store['info'] = info
    store['marks'] = scores
    store['car1'] = c1
    store['car2'] = c2



