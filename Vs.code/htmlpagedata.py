import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
fhand= urllib.request.urlopen(url,context=ctx)
bdata = fhand.read()
html = bdata.decode()
print(html)