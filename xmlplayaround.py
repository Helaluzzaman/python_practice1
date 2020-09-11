#import urllib.request,urllib.error
import ssl
import xml.etree.ElementTree as et

fhand = open("xmlexample1.xml")
xmldata = fhand.read()

print(xmldata[:500])

xml = et.fromstring(xmldata)
print(type(xml), xml.tag, xml.attrib)
print("now game is starting: \n")
for i in xml.findall("comments/comment"):
    print(i[1].tag, i[1].text)