import pickle

with open("pickled.dat", "rb") as infile:
    a = pickle.load(infile)
    name = pickle.load(infile)
    info = pickle.load(infile)
    p = pickle.load(infile)

print "a = ", a
print "name = ", name
print "info = ", info

print "Person's name =", p.name
print "Person's city =", p.city
 

