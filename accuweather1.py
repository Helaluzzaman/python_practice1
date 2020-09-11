import urllib.request, urllib.parse, urllib.error
import ssl
import json

apikey = "qTMk70OlpxCcDqL1JHkUqKEl5GElZeGv"
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://dataservice.accuweather.com/locations/v1/search?"
latlan = input("city:")
param = dict()
param["q"] = latlan
param["apikey"] = apikey

url = serviceurl + urllib.parse.urlencode(param)
print(url)


fhand = urllib.request.urlopen(url, context = ctx)

data = fhand.read().decode()
if len(data) < 20:
    print(data)
# fhandw = open("accuweatherlocation+key.json","w")
# fhandw.write(data)
try:
    js = json.loads(data)
    print("json retrived", len(data), "character")
except:
    print("Failed !! so retry")
if len(data)>10: 
    print(json.dumps(js, indent = 4))

headers = dict(fhand.getheaders())
print("remaining:",headers)
print("remaining:",headers['RateLimit-Remaining'])

# key = js[0]["Key"]
# print("key", key)
# 30659   rangpur 30537, dhaka 28143, lalmonir hat 30547
# cmd = "http://dataservice.accuweather.com/currentconditions/v1/" + key + "?" + "apikey=qTMk70OlpxCcDqL1JHkUqKEl5GElZeGv"
# print(cmd)
# fhand2 = urllib.request.urlopen(cmd)
# data = fhand2.read().decode()
# print(data)
# print(fhand2.getheaders())











