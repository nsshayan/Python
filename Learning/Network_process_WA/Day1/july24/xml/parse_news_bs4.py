from bs4 import BeautifulSoup
from urllib import urlopen

news_url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"

contents = urlopen(news_url).read()

soup = BeautifulSoup(contents, features="xml")


for title in soup.select('channel item title'):
    print "-" * 30
    print title.string

print "-" * 30


