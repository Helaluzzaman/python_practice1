import urllib.request
fname = urllib.request.urlopen("file:///C:/Users/Hasib/Desktop/Python%20file/regex_sum_851788.txt")
print(fname.code)
text = fname.read().decode()
lst= list()
import re
nums = re.findall("[0-9]+",text)
inums=[int(i) for i in nums]  #or we can use map
#inums= list(map(int,nums))
print(sum(inums))