from urllib import urlopen
from sys import argv, stderr
import re
from extract_links import extract_links

def crawl(url, broken_link, traversed):
    response = urlopen(url)
    if response.code != 200:
        broken_link.append(url)
        return

    for link in extract_links(response.read()):
        if not link.startswith("#") and link != url and link not in traversed:
            if link.startswith("http") and link.startswith(url): 
                crawl(link, broken_link, traversed)
                traversed.add(link)
        

if len(argv) < 2: 
    print "usage: %s URL." % argv[0]
    exit(1)

try:
    broken_links = []
    traversed = set([])
    crawl(argv[1], broken_links, traversed)
finally:
    print broken_links
    print "-" * 40
    print traversed


