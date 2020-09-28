import json
a = {"name": "John", "visited": ("Delhi","Kolkatta", "Hyderabad"), "present": False, "test": None}
a
json.dumps(a)
with open("testfile.json", "w") as outfile: json.dump(a, outfile)
j = json.dumps(a)
print(j)
with open("testfile.json") as infile: b = json.load(infile)
b
with open("testfile.json") as infile: b = json.load(infile)
dir(json)
help(json)
help(json.load)
a
b
with open("testfile.json") as infile: data = infile.read()
data
data.split()
data.splitlines()
data.splitlines()[0]
data.splitlines()[1]
with open("testfile.json") as infile:
    for line in infile:
        print(json.loads(line))
import xml.etree.ElementTree as et
et
dir(et)
et.parse?
xml = et.parse("books.xml")
import os
os.getcwd()
os.chdir("xml")
xml = et.parse("books.xml")
xml
xml.getroot()
c = xml.getroot()
c
c.text
c.name
dir(c)
c.tag
c[0]
c[1]
c[2]
c[0][0]
c[0][0].text
len(c)
for book in c:
    print(book[0].text)
c[0][1]
c[0][1].text
c[0]
c[0].attrib
c[0].attrib["id"]
for book in c: print(book.attrib["id"])
c
c.find("./book")
c.find("./book/title")
c.findall("./book/title")
c.findall("./book/title/text()")
c.findall("./book/title")
[ t.text for t in c.findall("./book/title") ]
c.iterfind("./book/title")
for t in c.iterfind("./book/title"): print(t.text)
c.findall("./book[@id='bk105']")
c.find("./book[@id='bk105']")
c.find("./book[@id='bk105']/title")
c.find("./book[@id='bk105']/title").text
c.find("./book[@id]")
c.find("./book[@id]").text
c.find("./book[@id]/title").text
c.find("./book[@id='bk101']/title").text
c.find("./book[author='Ralls, Kim']/title").text
c.find(".//title").text
c
c[-1]
c[-1][0].text
c[:3]
c[-3:]
c[3]
c[3][0]
c[3][0].text
c[3][0].text = "Chandrashekar"
c[3][0].text
xml
dir(xml)
xml.write?
xml.write("newbook.xml")
c[:]
c[0][:]
c[0][-1]
del c[0][-1]
c[0][:]
xml.write("newbook.xml")
c
dir(c)
c.makeelement?
c.makeelement("foo")
c.makeelement("foo", {})
f = c.makeelement("foo", {})
f.text = "this is a test string"
f
f.tag
f.text
c[1]
c[1].insert(f)
c[1].insert?
c[1].insert(2, f)
c[1][:]
c[2].append(f)
xml.write("newbook.xml")
c.find("./book[@id='bk104']")
c.find("./book[@id='bk104']").attrib
c.find("./book[@id='bk104']").attrib["id"] = "bk200"
xml.write("newbook.xml")
import xml.etree.ElementTree as et
import lxml.etree as et2
et.parse("books.xml")
et2.parse("books.xml")
lxml = et2.parse("books.xml")
xml
lxml
lxml.getroot()
catalog = lxml.getroot()
catalog.find("./book")
catalog.find("./book/title")
catalog.find("./book/title").text
catalog.xpath("./book/title")
catalog.xpath("./book/*")
catalog.xpath("./book[0]/*")
catalog.xpath("/book[0]/*")
catalog.xpath("/book/*")
catalog.xpath("./book[@id='bk101'/*")
catalog.xpath("./book[@id='bk101']/*")
catalog.xpath("./book/title[name()='Midnight Rain']")
catalog.xpath("./book/title[name()='Midnight Rain']/")
catalog.xpath("./book/title/[name()='Midnight Rain']/")
catalog.xpath("./book/title/[name()='Midnight Rain']")
catalog.xpath("./book")
catalog.xpath("./book/last()")
catalog.xpath("./book[last()]")
catalog.xpath("./book[1]")
catalog.xpath("./book[0]")
catalog.xpath("./book[2]")
catalog.xpath("./book[3]")
catalog.xpath("./book[count(*)]")
dir(catalog)
catalog
catalog.cssselect("book author")
p = et2.parse("purchase_order_example.xml")
p
dir(p)
p.xmlschema?
schema = et2.parse("po.xsd")
schema
p.xmlschema(schema)
from bs4 import BeautifulSoup
bs = BeautifulSoup(open("books.xml"))
bs = BeautifulSoup(open("books.xml"), "lxml")
bs = BeautifulSoup(open("books.xml"), "lxml")
dir(bs)
import untangle
untangle.parse("books.xml")
t = untangle.parse("books.xml")
t
t.catalog
t.catalog.book
t.catalog.book["id"]
t.catalog[0].book["id"]
t.catalog[0]
t.catalog
t.catalog.book[0]
t.catalog.book[0]["id"]
t.catalog.book[0].author
t.catalog.book[0].author.cdata
t.catalog.book[0].author.name
t.catalog.book[0].author
import xmltodict
xmltodict?
dir(xmltodict)
xmltodict.parse?
xmltodict.parse(open("books.xml"))
xmltodict.parse(open("books.xml").read())
xml = xmltodict.parse(open("books.xml").read())
xml
json
json.dumps(xml)
import lxml.etree
import lxml.html as html
import urllib
dir(urllib)
import urllib.parse
dir(urllib.parse)
urllib.parse.quote("hello world")
urllib.parse.quote("name=john&age=40")
q = urllib.parse.quote("name=john&age=40")
q
urllib.parse.unquote(q)
n = urllib.parse.unquote(q)
n
urllib.parse.parse_qs(n)
d = {"name": "sam", "role": "admin", "dept": "IT"}
d
urllib.parse.unparse(d)
dir(urllib.parse)
urllib.parse.urlunparse(d)
urllib.request
dir(urllib.request)
dir(urllib.request)
pip3 install requests
import requests
r = requests.get("http://www.chandrashekar.info")
r
r.status_code
r.ok
r.headers
r.headers["content-type"]
for k, v in r.headers.items(): print(k, v)
r.text
r.content
r.json()
r = requests.get("https://jsonplaceholder.typicode.com")
r
r.headers["content-type"]
r = requests.get("https://jsonplaceholder.typicode.com/users")
r.headers["content-type"]
r.text
r.json()
r.json()
r.json()[0]
a = r.json()[0]
a
a["address"]["city"] = "Bengaluru"
a["name"]
a["name"] = "Chandrashekar"
a
requests.post("https://jsonplaceholder.typicode.com/users", json=a)
dir(requests)
requests.request?
requests.get("https://www.chandrashekar.info")
requests.get("https://www.chandrashekar.info", verify=False)
requests.get("https://www.chandrashekar.info", verify=False)
r = requests.get("http://www.chandrashekar.info")
r
r
r.cookies
r = requests.get("http://www.google.com")
r
r.cookies
r.url
r = requests.get("http://www.google.com", redirect=False)
requests.request?
r = requests.get("http://www.google.com", allow_redirects=False)
r.url
r.status_code
r.headers["location"]
requests.request?
import robobrowser
from robobrowser import RoboBrowser
b = RoboBrowser(parser="lxml.html")
b
b.open("http://www.chandrashekar.info")
b.url
b.contents
b.response
b.response.status_code
b.links
dir(b)
b.get_links()
b = RoboBrowser(parser="lxml")
b.open("http://www.chandrashekar.info")
b.get_links()
b.get_links()
b.forms
dir(b)
b.get_links()
b.get_links()[-3]
l = b.get_links()[-3]
b.follow_link(l)
b.url
b.back()
b.url
b.forward()
b.url
b.get_forms()
b.get_forms()[0]
f = b.get_forms()[0]
f
f["name"] = "smith"
f["subject"] = "dslfj lsdjf lsdjf lksdj flsdjf"
f
b.submit_form(f)
import requests
r = requests.get("http://pypi.python.org/pypi", params={":action" : "search",
                               "term" : term,
                               "submit" : "search"})
r = requests.get("http://pypi.python.org/pypi", params={":action" : "search",
                               "term" : "rest",
                               "submit" : "search"})
r
r.headers
r.content
from robobrowser import RoboBrowser
b = RoboBrowser()
b = RoboBrowser()
b.open("http://www.chandrashekar.info/user/login")
b.url
b.get_form(id="user-login")
b = RoboBrowser(parser="lxml")
b.open("http://www.chandrashekar.info/user/login")
b.get_form(id="user-login")
login_form = b.get_form(id="user-login")
login_form["name"] = "testuser"
login_form["pass"] = "w3lc0me"
login_form
b.submit_form(login_form))
b.submit_form(login_form)
b.response.ok
b.url
b.get_links()
b.get_link(text="View recent blog entries")
v = b.get_link(text="View recent blog entries")
b.follow_link(v)
b.url
b.get_link(text="Post new blog entry")
p = b.get_link(text="Post new blog entry")
b.follow_link(p)
b.url
b.get_form(id="blog-node-form")
blog_form = b.get_form(id="blog-node-form")
blog_form["title"] = "a test blog - chandrashekar - dec 21"
blog_form["body[und][0][summary]"] = "sldfj klsdj flksd jlksdj klsdf"
blog_form["body[und][0][value]"] = "sldfj klsdj flksd jlksdj klsdf sdf ksd fksdflsdjfdsfsf"
blog_form["op"]
blog_form["op"] = "Save"
blog_form["op"]
b.submit_form(blog_form)
b.submit_form(blog_form, submit="Save")
blog_form
blog_form["op"]
blog_form["op"][0]
dir(blog_form["op"])
blog_form["op"].name
blog_form["op"].value
blog_form["op"] = "Save"
b.submit_form(blog_form, submit=blog_form["op"])
b.url
%help
help
%save
%save ipython_history.py
%save "ipython_history.py"
%save
%save a
%help
%create
?
%quickref
%save testfile
%history
%save
%save a
%save %history
%history -f transcript.py
