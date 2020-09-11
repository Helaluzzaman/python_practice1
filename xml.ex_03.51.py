import urllib.request,urllib.error
import ssl
import xml.etree.ElementTree as et

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
fhand = urllib.request.urlopen(url, context = ctx)
xmldata = fhand.read().decode()

xml = et.fromstring(xmldata)
lst = xml.findall("comments/comment/count")
nlst = [ int(i.text) for i in lst]
print(sum(nlst))
