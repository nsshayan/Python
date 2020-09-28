import xml.etree.ElementTree as xml
from urllib2 import urlopen

#rss_url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"

#f = urlopen(rss_url)

f = open("news.xml")
contents = f.read()

rootElement = xml.fromstring(contents)
#rootElement = tree.getroot()

for item in rootElement.findall('channel/item'):
    print "=" * 40
    print item.find(u"title").text
    print "-" * 40
    print unicode(item.find(u"description").text)


#for title in rootElement.findall('channel/item/title'):
#    print "-" * 30
#    print title.text

print "-" * 30

#for title in rootElement.getiterator('title'):
#    print title.text

