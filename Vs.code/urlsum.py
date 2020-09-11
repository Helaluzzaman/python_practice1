import urllib.request
fhand = urllib.request.urlopen("file:///C:/Users/Hasib/Desktop/Python%20file/regex_sum_851788.txt")
text = fhand.read().decode()
import re
nums = re.findall("[0-9]+",text)
inums = list(map(int,nums))
print(sum(inums))