from pickle import dumps
from person import Person

p = Person("Sam", 55, "Mumbai")

print dumps(p)

