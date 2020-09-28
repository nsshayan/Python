from bs4 import BeautifulSoup
import requests
resp = requests.get("https://finance.yahoo.com/quote/CSCO/options?p=CSCO")

html = resp.content
soup = BeautifulSoup(html, "lxml")

options = soup.find_all("option")
print(options)

from requests_html import HTMLSession
    
session = HTMLSession()
resp = session.get("https://finance.yahoo.com/quote/CSCO/options?p=CSCO")
resp.html.render()
current_quote = resp.html.xpath(".//span[@data-reactid='32']/text()")
print("Current stock quote =", current_quote)

#options = resp.html.find("option")
#print(option_tags)
#for o in options:
#    print(o.text, o.attrs["value"])
