import urllib.request
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen("file:///C:/Users/Hasib/Desktop/Python%20file/Vs.code/htmltest.html")
html = fhand.read()

soup = BeautifulSoup(html, "html.parser")
print(type(soup))
tags = soup("a")
print(tags)
print(dir(tags))
for tag in tags[0:1]:
    attrib = tag
    print(type(attrib), "dir", dir(attrib) )