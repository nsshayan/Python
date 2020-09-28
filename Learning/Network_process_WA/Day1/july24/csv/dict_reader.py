from csv import DictReader, writer

with open("a.csv") as f, open("b.csv", "w") as out:
    
    output = writer(out)
    output.writerow(["Age", "Location"])

    for row in DictReader(f):
        print row["AGE"], "|", row["Location"]
        output.writerow([row["AGE"], row["Location"]])

from os import rename
rename("b.csv", "a.csv")

