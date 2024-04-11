import requests
import sys

res = requests.get(url="https://api.apis.guru/v2/list.json")  #this is an example api
print(res)

data = res.cookies
print(data)
