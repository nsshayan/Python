import csv

with open("a.csv") as artists, open("b.csv") as songs:
    a = csv.reader(artists, delimiter=',')
    b = csv.reader(songs, delimiter=",")

    for (name,age,city),(song,year) in zip(a, b):
        print name, age, city, song, year
