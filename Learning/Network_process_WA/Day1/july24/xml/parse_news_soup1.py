from bs4 import BeautifulSoup
from urllib.request import urlopen

News_Url = "http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms"

response = urlopen(News_Url)

soup = BeautifulSoup(response, "xml")


for title in soup.select('channel item title'):
    print("-" * 30)
    print(title.string)

print("-" * 30)
