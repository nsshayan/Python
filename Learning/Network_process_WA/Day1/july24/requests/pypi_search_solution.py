import requests
import sys

if len(sys.argv) < 2:
    print("usage: %s package" % sys.argv[0])
    exit(1)

search = sys.argv[1]

response = requests.get("http://pypi.python.org/")
if response.status_code != 200:
    print("Failed to initiate request...")
    exit(1)

response = requests.get("http://pypi.python.org/pypi",
                        {":action" : "search",
                         "term" : search,
                         "submit" : "search"},
                        cookies=response.cookies)


print(response.status_code)
print("-" * 30)
if response.status_code == 200:
    print(response.text.encode("utf-8"))

