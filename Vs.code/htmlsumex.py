import urllib.request
fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_851790.html")
html = fhand.read().decode()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
tags = soup("span")
nums = list()
for tag in tags:
    nums.append(int(tag.contents[0]))
print(sum(nums))
