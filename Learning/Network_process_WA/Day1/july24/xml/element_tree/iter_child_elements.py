import xml.etree.ElementTree as et
tree = et.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

print("-" * 20)
print(root[0])
print(root[0][1])
print(root[0][1].text)

