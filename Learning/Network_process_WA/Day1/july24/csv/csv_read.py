import csv

with open("a.csv") as f:
    records = csv.reader(f)
    for name, age, location in records:
        print "Name: %s, Age: %s, Location: %s" % (name, age, location)
    #for rec in records:
    #    name, location = rec[0], rec[2]

