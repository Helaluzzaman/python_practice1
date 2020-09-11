#using lat, lan
import urllib.request, urllib.parse, urllib.error
import ssl
import json

apikey = "qTMk70OlpxCcDqL1JHkUqKEl5GElZeGv"
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search.json?"
latlan = input("lat,lan:")
param = dict()
param["q"] = latlan
param["apikey"] = apikey

url = serviceurl + urllib.parse.urlencode(param)
print(url)


fhand = urllib.request.urlopen(url, context = ctx)

data = fhand.read().decode()
fhandw = open("accuweatherlocation+key.json","w")
fhandw.write(data)
try:
    js = json.loads(data)
    print("json retrived", len(data), "character")
except:
    print("Failed !! so retry")
print(json.dumps(js, indent = 4))

headers = dict(fhand.getheaders())
print("remaining:",headers)
print("remaining:",headers['RateLimit-Remaining'])