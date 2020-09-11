import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/")
print(fhand.code)
html = fhand.read().decode()
print(html)
file = open("htmltest.txt","w")
file.write(html)
file.close()
