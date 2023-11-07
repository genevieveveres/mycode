import requests
import urllib.request
import json

url= "http://api.open-notify.org/astros.json"

response= requests.get(url) #get requests are most common
    #.post()
    #.put()
    #.delete()

print(response.status_code)
print(response.url)

##jsondata = response.text
#jsondata= response.json()
#print(jsondata["authors"])

response = urllib.request.urlopen(url)
scraped= response.read()
workingstring= scraped.decode("utf-8")
jsondata= json.loads(workingstring)

print(jsondata["number"])
