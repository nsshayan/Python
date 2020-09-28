from bs4 import BeautifulSoup
import requests
resp = requests.get("https://finance.yahoo.com/quote/NFLX/options?p=NFLX")

html = resp.content
soup = BeautifulSoup(html, "lxml")

options = soup.find_all("option")
print(options)

from requests_html import HTMLSession

session = HTMLSession()
resp = session.get("https://finance.yahoo.com/quote/NFLX/options?p=NFLX")
resp.html.render()
options = resp.html.find("option")
#print(option_tags)
for o in options:
    print(o.text, o.attrs["value"])

