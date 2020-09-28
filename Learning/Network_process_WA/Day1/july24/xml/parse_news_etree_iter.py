import xml.etree.ElementTree as et
import urllib

news_url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"
url = urllib.urlopen(news_url)

rootElement = et.fromstring(url.read())

for title in rootElement.finditer('channel/item/title'):
    print "-" * 30
    print title.text

print "-" * 30


