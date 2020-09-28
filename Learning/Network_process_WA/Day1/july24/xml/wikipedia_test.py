import requests
from time import sleep

for i in range(10):
    res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    if res.status_code == 200:
        print(res.url)
    sleep(1)



