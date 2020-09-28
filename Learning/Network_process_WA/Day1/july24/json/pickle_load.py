from pickle import loads
from sys import stdin

p = loads(stdin.read())

print "Name: ", p.name
print "Age: ", p.age
print "City: ", p.city

