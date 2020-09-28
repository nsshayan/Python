import xml.etree.ElementTree as et


doc = et.parse("test1.xml")

root = doc.getroot()

e = root.makeelement("email", {})
e.text = "john_doe@gmail.com"

root[0].append(e)

doc.write("test_new.xml")



