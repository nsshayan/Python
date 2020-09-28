from urllib import urlopen

with open("july11.zip", "w") as out:
    r = urlopen("http://www.chandrashekar.info/files/python/july11.zip")
    out.write(r.read())

