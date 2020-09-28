# IPython log file

get_ipython().run_line_magic('cd', '..')
get_ipython().run_line_magic('pwd', '')
ssh_info = {
    "192.168.56.101": {
        "username": "root",
        "password": "welcome",
        "logfiles": ["/var/log/pacman.log", "/var/log/system.log"]
    },

    "192.168.56.102": {
        "username": "pythonista",
        "password": "welcome",
        "logcommands": ["/usr/bin/dmesg", "/usr/bin/journalctl"]

    }

}
ssh_info
import json
json.dumps(ssh_info)
a = {"name": "john", "active": False, "visited": None, "places": ("Bengaluru", "Chennai", "Kolkatta")}
a
with open("a.json", "w") as outfile:
    json.dump(a, outfile)
    
get_ipython().run_line_magic('cat', 'a.json')
get_ipython().run_line_magic('cat', 'a.json')
with open("a.json") as infile:
    b = json.load(infile)
    
b
import xml.etree.ElementTree as et
et
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', 'xml')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('cat', 'books.xml')
import xml.etree.ElementTree as et
tree = et.parse("books.xml")
tree
c = tree.getroot()
c
c.attrib
c.text
c[0]
c[1]
c[2]
c[0]
c[0].attrib
c[1].attrib
c[-1].attrib
len(c)
c[:5]
[ b.attrib["id"] for b in c ]
c[0]
c[0][0]
c[0][0].text
c[0][0].text = "Babu, Chandrashekar"
len(c)
c[-1][0].text
del c[-1]
get_ipython().run_line_magic('pinfo', 'c.makeelement')
c.makeelement("country", {"code": "IN"})
e = c.makeelement("country", {"code": "IN"})
e
e.text = "India"
c[0]
c[0][0]
c[0].append(e)
tree.write("newbook.xml")
c.find("./book")
c.find("./book/author")
c.find("./book/title")
c.find("./book/title").text
c.findall("./book/title")
[ t.text for t in c.findall("./book/title") ]
c.findall("./book[author='Corets, Eva']")
c.findall("./book[author='Corets, Eva']/title")
[ t.text for t in c.findall("./book[author='Corets, Eva']/title") ]
c.iterfind("./book[author='Corets, Eva']/title")
for t in c.iterfind("./book[author='Corets, Eva']/title"):
    print(t.text)
    
[ t.text for t in c.iterfind("./book[author='Corets, Eva']/title") ]
c.findall("./book[@id='bk105']")
c.findall("./book[@id='bk105']/title")
c.find("./book[@id='bk105']/title")
c.find("./book[@id='bk105']/title").text
c.findall("./book[price > 5]")
c.findall("./book[price gt 5]")
c.findall("./book['price > 5']")
c.findall(".//author")
import lxml.etree as et1
et1.parse("books.xml")
tree1 = et1.parse("books.xml")
tree
tree1
dir(tree)
dir(tree1)
tree1.getroot()
c1 = tree1.getroot()
c1[0]
c1.find("./book/author")
c1.findall("./book/author")
c1.xpath("./book/author")
c1.xpath("./book/author/text()")
c1.xpath("./book[price > 5]
c1.xpath("./book[price > 5]")
c1.xpath("./book[price > 5]/title/text()")
c1.xpath("./book[price < 5]/title/text()")
dir(c)
dir(c1)
get_ipython().run_line_magic('logstart', '')
from bs4 import BeautifulSoup
with open("books.xml") as books:
    soup = BeautifulSoup(books.read())
    
with open("books.xml") as books:
    soup = BeautifulSoup(books.read(), "lxml")
    
    
type(soup)
soup
with open("books.xml") as books:
    soup = BeautifulSoup(books.read(), "lxml")
 
soup.html
soup.html.body
soup.html.body.catalog
soup.html.body.catalog.book
soup.html.body.catalog.book.author
soup.html.body.catalog.book
soup.html.body.catalog.book.next()
soup.html.body.catalog.book.next_sibling()
soup.html.body.catalog.book.next_sibling
soup.html.body.catalog.book.next
soup.html.body.catalog.book.next.next
soup.html.body.catalog.book.next.next.next
soup.html.body.catalog.book.next.next.next.next
dir(soup)
import lxml.html as html
doc = html.parse("index.html")
doc
doc.findall(".//a[@href]")
doc.xpath(".//a[@href]")
doc.xpath(".//a[@href]/text()")
doc.xpath(".//a[@href]/@href")
doc.xpath(".//a[@href != 'javascript:void(0);']/@href")
doc.xpath(".//input")
doc.xpath(".//input[@type = 'text']")
doc.xpath(".//form")
dir(doc)
doc
doc.html
doc.getroot()
h = doc.getroot()
dir(h)
h.cssselect("html body div")
h.cssselect("html body div span")
h.cssselect("html body div span#title")
import requests
response = requests.get("http://www.chandrashekar.info")
reponse
response
response.status_code
response.headers
response.headers["content-type"]
response.text
response.content
type(response.content)
type(response.text)
response.url
r = requests.get("http://www.google.com/")
r
r.url
r.status
r.status_code
r.cookies
session = requests.Session()
session
s = session.get("http://www.cisco.com")
s
s.status_code
s.headers["content-type"]
r.text
r.cookies
s.headers
s.cookies
requests.get
requests.post
requests.put
requests.delete
requests.head
requests.patch
r = requests.get("pypi.org")
r = requests.get("http://pypi.org")
r
r.text
html
html.fromstring(r.text)
h = html.fromstring(r.text)
h.find(".//form")
r
r = requests.get("http://pypi.org/search/?q=rest")
r
r.text
h = html.parse(r.text)
h = html.fromstring(r.text)
h
with open("result.html", "w") as out: out.write(r.text)
get_ipython().run_line_magic('pwd', '')
h.xpath(".//div[@class='package-snippet']")
h.xpath(".//div[@class='package-snippet']")[:5]
result = h.xpath(".//div[@class='package-snippet']")[:5]
result[0]
result[0][0]
result[0][0][0]
result[0][0][0].attrib["href"]
result = h.xpath(".//div[@class='package-snippet']/h3/a")[:5]
result
r = requests.get("http://pypi.org/search/?q=xml")
r.status_code
r.ok
r.text
regex = r'''
<h3 class="package-snippet__title">
'''
re.search(regex, r.text)
import re
re.search(regex, r.text)
r.text
re.search(regex, r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search(regex, r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search("h3", r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search("<h3 class=", r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search("<h3\s+class=", r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
regex = r'''
<h3 \s+ class="package-snippet__title">
'''
re.search("<h3\s+class=", r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
regex = r'''
<h3 \s+ class="package-snippet__title">
\s*<a \s+ href="(?P<url>.+?)">
'''
re.search("<h3\s+class=", r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search(regex, r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search(regex, r.text, re.VERBOSE | re.MULTILINE | re.DOTALL).groupdict()
regex = r'''
  <h3 \s+ class = "package-snippet__title" > \s* 
      <a \s+ href="(?P<url>.+?)">            \s*   # <a href='url'>
      (?P<name>.+?)                          \s*   # name
   </a>
'''
re.search("<h3\s+class=", r.text, re.VERBOSE | re.MULTILINE | re.DOTALL)
re.search(regex, r.text, re.VERBOSE | re.MULTILINE | re.DOTALL).groupdict()
regex = r'''
  <h3 \s+ class = "package-snippet__title" > \s* 
      <a \s+ href="(?P<url>.+?)">            \s*   # <a href='url'>
      (?P<name>.+?)                          \s*   # name
   </a>                                      \s*
   .+?
   <p \s+ class="package-snippet__description"> \s*
   (?P<description>.+?)                      \s*
   </p> 
'''
re.search(regex, r.text, re.VERBOSE | re.MULTILINE | re.DOTALL).groupdict()
re.compile(regex, re.VERBOSE | re.MULTILINE | re.DOTALL)
p = re.compile(regex, re.VERBOSE | re.MULTILINE | re.DOTALL)
for m in p.finditer(r.text):
    print(m.groupdict())
    
get_ipython().run_line_magic('paste', '')
package-snippet__titl
get_ipython().run_line_magic('paste', '')
package-snippet__titl
get_ipython().run_line_magic('copy', '')
get_ipython().run_line_magic('clip', '')
with open("re.out", "w") as out: out.write(regex)
get_ipython().run_line_magic('cat', 're.out')
a = {"index": 1}
a
b = {"url": "sfsdf", "name": "werwer"}
a
b
c = a + b
c = **a, **b
c = dict(**a, **b)
c
c = dict(**dict(index=0), **b)
c
r
r.text
import lxml.html as html_parser
html = html_parser.fromstring(r.text)
html
html.xpath(".//div[@class='package-snippet']")
html.xpath(".//div[@class='package-snippet']")[:5]
snippets = html.xpath(".//div[@class='package-snippet']")[:5]
snippet = snippets[0]
snippet
snippet[0]
snippet[0].text
snippet.xpath("./h3/a")
a = snippet.xpath("./h3/a")
a.text
a
[ a.text, a.url for a in snippet.xpath("./h3/a") ]
[ (a.text, a.url) for a in snippet.xpath("./h3/a") ]
[ (a.text, a.url) for a in snippet.xpath("./h3/a") ]
[ (a.text, a.attrib["href"]) for a in snippet.xpath("./h3/a") ]
[ dict(name=a.text, url=a.attrib["href"]) for a in snippet.xpath("./h3/a") ]
snippets
snippet
snippet.xpath("./h3/a")
snippet.xpath("./h3/a")[0]
snippet.find("./p")
snippet.find("./p").text
requests.get("http://localhost:3000/users")
requests.get("http://localhost:3000/werwer")
requests.get("http://localhost:3000/werwer").ok
requests.get("http://localhost:3000/users")
r = requests.get("http://localhost:3000/users")
r.ok
r.headers["content-type"]
r.json()
r = requests.get("http://localhost:3000/users")
r.json()
requests.post("http://localhost:3000/users", json={"name": "jones", "role": "developer", "email": "jones@yahoo.com"})
r.text
requests.get("http://localhost:3000/users").json()
requests.get("http://localhost:3000/users/3")
requests.get("http://localhost:3000/users/3").json()
r = requests.patch("http://localhost:3000/users/3", json={"email": "jones@cisco.com"})
r
r.json()
requests.get("http://localhost:3000/users").json()
r = requests.delete("http://localhost:3000/users/2")
r
r.json()
requests.get("http://localhost:3000/users").json()
get_ipython().run_line_magic('run', '../open_weather_api.py')
forecast_url
weather_url
weather_url.format(CITY="Bengaluru", APIKEY=api_key)
q = weather_url.format(CITY="Bengaluru", APIKEY=api_key)
r = requests.get(q)
r
r.ok
r.json()
from robobrowser import RoboBrowser
br = RoboBrowser(parser="lxml")
br
br.open("http://pypi.org/")
br.response
br.response.ok
br.url
br.get_links()
br.get_link("Register)
br.get_link("Register")
br.get_link(text="Register")
br.get_link()
get_ipython().run_line_magic('pinfo', 'br.get_link')
br.get_link(text="Register")
br.get_link(text_re="Register")
br.get_forms()
br.get_form()
f = br.get_form()
f["q"]
f["q"] = "xml"
br.submit_form(f)
br.url
br.response.ok
br.find("div")
br.open("http://www.chandrashekar.info/")
br.url
br.get_links()
br.get_link("Contact")
l = br.get_link("Contact")
br.follow_link(l)
br.url
br.back()
br.url
br.forward()
br
br.get_forms()
br.open("http://pypi.org/search/?q=xml")
br.response.ok
dir(br)
br.select("div.package-snippet")
len(br.select("div.package-snippet"))
br.select("div.package-snippet")[:5]
snippets = br.select("div.package-snippet")[:5]
s = snippets[0]
s
s.a
s.a["href"]
s.a["href"], s.a.text
s.p.text
enumerate(br.select("div.package-snippet")[:5], 1)
[ x for x in enumerate(br.select("div.package-snippet")[:5], 1)]
[ x for x in enumerate(br.select("div.package-snippet")[:5], 1)][0]
[ dict(index=i, name=d.a.text, url=d.a["href"], description=d.p.text) for i, d in enumerate(br.select("div.package-snippet")[:5], 1)]
br
br.open("http://pypi.org/search/?q=xml")
br.response.ok
br.parsed
br.select("div.package-snippet")
br.select("div.package-snippet")[:5]
result = br.select("div.package-snippet")[:5]
result[0]
r = result[0]
r
r.a
r.a.text
r.a["href"]
r.p.text
[ (r.a.txt, r.a["href"], r.p.text) for r in result ]
[ (r.a.text, r.a["href"], r.p.text) for r in result ]
b = RoboBrowser(parser="lxml")
b.open("http://www.fincher.org/tips/web/SimpleForm.shtml")
b.get_forms()
b.get_form()
b.select("input")
b.open("http://www.html.am/html-codes/forms/")
b.get_forms()
f = b.get_form()
f
f["color"] = "Red"
f["color"]
f["color"]
f["color"] = 1
f["color"]?
get_ipython().run_line_magic('pinfo', 'f')
dir(f["color"])
f["color"].labels
f["color"].value
f["color"].value = "Red"
f["color"].value = "Red\r\n"
f["color"].value = "Red\r\n"
f["color"].value
f["color"]
f["color"].labels
dir(f["color"])
f["color"] = "Red\r\n"
dir(f["color"])
f["color"].labels
f["color"].value = ' Red\r\n'
f["color"] = ' Red\r\n'
f
b
b
b.open("http://www.chandrashekar.info/user/login")
b.url
b.get_forms()
b.get_form()
b.get_form(form_id="user_login")
b.get_form(form_id=user_login)
login = b.get_form(id="user-login")
login
login["name"] = "testuser"
login["pass"] = "w3lc0me"
login
b.submit_form(login)
b.url
b.get_links()
b.get_link("View recent blog entries")
b.follow_link(b.get_link("View recent blog entries"))
b.url
b.get_link("Post new blog")
b.follow_link(b.get_link("Post new blog"))
b.url
b.get_forms()
b.get_form(id="node-blog-form")
b.get_form(id="blog-node-form")
blog = b.get_form(id="blog-node-form")
blog
blog["title"] = "new blog - june 1st 2018 from chandrashekar"
blog["body[und][0][summary]"] = "sdf lsd fls dflksdklf jsdlkf jsdlkf sldkflksdfjsd"
blog["body[und][0][value]"] = "sdf lsd fls dflksdklf jsdlkf jsdlkf sldkflksdfjsd"
blog["op"]
blog["op"].value
blog["op"] = "Save"
b.submit_form(blog, blog["op"])
b.url
"new blog - june 1st 2018 from chandrashekar" in b.parsed.text
blog["op"] = "werwer"
b.submit_form(blog, blog["op"])
b.url
from selenium.webdriver.common.keys import Keys
dir(Keys)
Keys.ENTER
Keys.ALT
