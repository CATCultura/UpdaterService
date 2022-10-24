import json

import requests
#
# file = open('service/Persistence/current_data.json', 'r', encoding='utf-8')
#
# data = json.load(file)
#
# url = "http://10.4.41.41:8081/event"
#
# for event in data:
#     req = requests.post(url, json=event)
#     if req.status_code != 200:
#         print(req.status_code)
#     else:
#         print("success")

file = open('users.json', 'r', encoding='utf-8')

data = json.load(file)

url = "http://10.4.41.41:8081/users"

for user in data:
    req = requests.post(url, json=user)
    if req.status_code != 200:
        print(req.status_code)
    else:
        print("success")
