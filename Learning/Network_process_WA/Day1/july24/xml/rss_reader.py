import xml.etree.ElementTree as xml
from urllib2 import urlopen


def fetch_rss(url):
    rootElement  = xml.fromstring(urlopen(url).read())

    for item in rootElement.findall('channel/item'):
        yield item.find("title").text, item.find("description").text

if __name__ == '__main__':
    rss_url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"

    for title, description in fetch_rss(rss_url):
        print title
        print "=" * 60
        print description
        print "-" * 60

