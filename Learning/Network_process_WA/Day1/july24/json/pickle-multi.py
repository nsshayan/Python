import pickle
from person import Person

a = [10, 20, 30]
name = "john"
info = {'name' : "sam", 'age' : 10, 'city' : 'Chennai' }

p = Person("john", 45, "delhi")

with open("pickled.dat", "wb") as out:
    pickle.dump(a, out)
    pickle.dump(name, out)
    pickle.dump(info, out)
    pickle.dump(p, out)

