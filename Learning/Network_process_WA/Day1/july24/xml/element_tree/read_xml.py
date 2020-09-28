import xml.etree.ElementTree as et
tree = et.parse('country_data.xml')
print(tree)
print("-" * 20)

root = tree.getroot()
print(root)
print(root.tag)

root = et.fromstring(open('country_data.xml').read())
print(root)
print(root.tag)

