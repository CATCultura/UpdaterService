import json

import requests

file = open('users.json', 'r', encoding='utf-8')

data = json.load(file)

url = "http://40.113.160.200:8081/users"

for user in data:
    req = requests.post(url, json=user)
    if req.status_code != 200:
        print(req.status_code)
    else:
        print("success")
