import requests
import sys

for
res = requests.get(url=f"http://google.com")
print(res)

data = res.cookies
print(data)
