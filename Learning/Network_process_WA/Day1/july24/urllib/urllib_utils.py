import urllib.parse
print(urllib.parse.quote("hello world"))

print(urllib.parse.quote("name=john&age=40"))
q = urllib.parse.quote("name=john&age=40")

print(q)
print(urllib.parse.unquote(q))
n = urllib.parse.unquote(q)
print(n)

print(urllib.parse.parse_qs(n))
d = {"name": "sam", "role": "admin", "dept": "IT"}

print(d)
# print(urllib.parse.unparse(d))
# dir(urllib.parse)
# print(urllib.parse.urlunparse(d))
