
import requests
import json

res=requests.get('https://randomuser.me/api?results=10&nat=AU,DE')
res=res.json()
result=res["results"]

for i in result:
    print(i["name"])
    print(i["nat"])