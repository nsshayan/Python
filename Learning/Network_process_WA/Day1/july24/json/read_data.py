from pickle import load

with open("data.dat") as f:
    a = load(f)
    b = load(f)
    c = load(f)

a.drive()
b.drive()
print c

