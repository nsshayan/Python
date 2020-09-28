from BeautifulSoup import BeautifulSoup

r = BeautifulSoup(open("out.xml").read())

print r.prettify()


