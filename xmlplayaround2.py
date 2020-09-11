import xml.etree.ElementTree as et

tree = et.parse("xmlexample1.xml")
print(type(tree))

root = tree.getroot()
x = [int(i.text) for i in root.findall("comments/comment/count")]
print(type(root), sum(x))