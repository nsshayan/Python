import urllib2
import re

hostname = "www.chandrashekar.info"

headers_list = """
Host: {host}:{port}
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.53.11 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
X-Purpose: preview
Accept-Language: en-us
Connection: keep-alive
""".format(host=hostname, port="80").splitlines()

header = { }
for line in headers_list:
    if not line: continue
    m = re.search("^([\w-]+):\s+(.+)$", line)
    if not m: continue
    k, v = m.group(1), m.group(2)
    header[k] = v

print "Header: ", header
print "-" * 40

req = urllib2.Request("http://" + hostname + "/user/login", "", header)
print "Fetching home page...",

res = urllib2.urlopen(req)
print "ok."


login_data = """
name=testuser&pass=w3lc0me&op=Log+in
"""

post_header = {
   "Host": "localhost:8080",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.53.11 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
   "Content-Length": len(login_data),
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Content-Type": "application/x-www-form-urlencoded",
   "Accept-Language": "en-us",
   "Connection": "keep-alive"
}

req = urllib2.Request("http://" + hostname + "/node?destination=tracker",
                      login_data, post_header)

print req

res = urllib2.urlopen(req)
print res

