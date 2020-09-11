# weather state getting by key:
import urllib.request, urllib.parse, urllib.error
import json
key = input("Enter location key: ")
apikey = input("api key (if have no left blank): ")
print("retriving data........")
if len(apikey) <3:
    apikey = "qTMk70OlpxCcDqL1JHkUqKEl5GElZeGv"
cmd = "http://dataservice.accuweather.com/currentconditions/v1/" + key + "?" + urllib.parse.urlencode({"apikey" : apikey, "details":"true"})
fhand = urllib.request.urlopen(cmd)

data = fhand.read().decode()

print(type(data))

try:
    js = json.loads(data)
    print("data retrived", len(data), "character")
    print(js)
except:
    js = None
 
if len(data)>10: 
    print(json.dumps(js, indent = 4))

header = fhand.getheaders()
for k, v in header:
    if k == "RateLimit-Remaining":
        print("Remain:", v)   
