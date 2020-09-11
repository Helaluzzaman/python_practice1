import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("file:///C:/Users/Hasib/Desktop/Python%20file/Vs.code/htmltest.html")
print(fhand.code)
html = fhand.read().decode()
print("Now Souping:")
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html.parser")
tags = soup("a")
print(tags)
#for tag in tags:
#    print(tag)
#    print("href:",tag.get("href"))
#    print("content:", tag.contents)
#    print("NEW", tag.attrs)