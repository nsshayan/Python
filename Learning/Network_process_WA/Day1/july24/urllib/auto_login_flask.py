from urllib2 import Request, urlopen
from urllib import urlencode

form_data = urlencode(dict(uname="john", passwd="welcome"))
req = Request("http://localhost:5000/login", form_data)

response = urlopen(req)

print response.code
print response.read()

