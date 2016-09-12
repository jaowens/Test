# samplewebservicecall.py
import requests
import json

url='http://www.google.com'

response= requests.get(url, verify=False)

print(response.text)

for item in response:
	print item