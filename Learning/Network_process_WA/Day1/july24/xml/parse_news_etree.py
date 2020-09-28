import xml.etree.ElementTree as et
import urllib

news_url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"
url = urllib.urlopen(news_url)

#tree = xml.parse('news.xml')
#rootElement = tree.getroot()

rootElement = et.fromstring(url.read())

for title in rootElement.findall('channel/item/title'):
    print "-" * 30
    print title.text

print "-" * 30

#for title in rootElement.getiterator('title'):
#    print title.text

