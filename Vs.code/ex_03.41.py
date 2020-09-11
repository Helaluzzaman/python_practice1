import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
serial = int(input("Enter serial:"))
times = int(input("Enter repeat times:"))



for i in range(1,(times+1)):
    fhand= urllib.request.urlopen(url,context=ctx)
    bdata = fhand.read()
    html = bdata.decode()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    #print(i,"href: ", tags[serial-1].get("href",None))
    url = tags[serial-1].get("href",None)
    name = str(tags[serial-1].contents[0])
    
    print(i,"Name: ",name)
    if i == times:
        print("result:",name )
    
    