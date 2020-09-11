import urllib.request
fname = urllib.request.urlopen("file:///C:/Users/Hasib/Desktop/Python%20file/regex_sum_851788.txt")

for line in fname:
    print(line.decode().rstrip())