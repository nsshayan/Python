from sys import argv
import lxml.html

if len(argv) < 2:
    print("usage: %s search-term" % argv[0])
    exit(1)

search_term = argv[1]

import requests
response = requests.get("http://pypi.python.org/pypi", {"term": search_term, "submit": "search",
                                             ":action": "search"})

if response.status_code == 200:
    html = lxml.html.fromstring(response.content)
    for tr in html.find('.//table')[1:6]:
        print("{:<15s} -- {:s}".format(tr[0][0].text, tr[2].text))

