import lxml.etree as etree
from urllib.request import urlopen

response = urlopen("http://www.chandrashekar.info/")

html = etree.parse(response, etree.HTMLParser())

print(html)
print(html.xpath("./head/title/text()"))


