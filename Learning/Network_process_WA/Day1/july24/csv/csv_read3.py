import csv

with open("a.csv") as a, open("b.csv") as b, open("c.csv", "w") as c:

    artists, songs = csv.reader(a), csv.reader(b)
    report = csv.writer(c)

    for (name, age, location), (song, year) in zip(artists, songs):
        report.writerow([name, age, song, year, location])

     

