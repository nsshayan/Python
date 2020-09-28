import csv

with open('a.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for name,age,city in r:
        print name, age, city
