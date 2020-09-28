from urllib2 import urlopen
from sys import argv, stderr
import os.path

if len(argv) < 2:
    print >>stderr, "usage: webget.py URL"
    exit(1)

path, fname = os.path.split(argv[1])

response = urlopen(argv[1])

with open(fname, "w") as f: f.write(response.read())

    

