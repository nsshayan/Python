from urllib import urlopen
from sys import argv, stderr
from extract_links import extract_links

if len(argv) < 2: 
    print "usage: %s URL." % argv[0]
    exit(1)

response = urlopen(argv[1])

for links in extract_links(response.read()): print links


