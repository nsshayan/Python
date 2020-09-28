import requests
import lxml.html as hp

url = "http://finance.yahoo.com/quote/CSCO"

#path = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div[3]/div[1]/div/span[1]/text()"
path = ".//h1[contains(text(), 'Cisco')]/following::span[2]/text()"
res = requests.get(url, params={"q": "CSCO"})
if res.ok:
   html = hp.fromstring(res.text)
   element = html.xpath(path)
   print(element)
   