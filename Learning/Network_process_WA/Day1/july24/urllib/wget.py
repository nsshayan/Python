import sys
from urllib import urlopen, urlencode

form_data = {
    "uname" : "john",
    "passwd" : "john123"
}

response = urlopen("http://localhost:7000/login.cgi", urlencode(form_data))

print response.read(),


