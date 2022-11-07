import json
import random
from collections import deque

import requests


def generate_list(id: int, ids: list) -> list:
    aux = random.sample(ids, random.randint(5, 10))
    if id in aux:
        aux.remove(id)
    return aux


def check_connection(check: dict, graph: dict, entry_point: int) -> bool:
    to_visit = deque()
    visited = [entry_point]
    for item in graph[entry_point]:
        to_visit.append(item)

    check[entry_point] = True
    while to_visit:
        current = to_visit.popleft()
        check[current] = True
        if current not in visited:
            visited.append(current)
            for item in graph[current]:
                if item not in to_visit and item not in visited:
                    to_visit.append(item)

    aux = set(visited)
    return len(visited) == len(graph.keys())


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
#
for user in data:
    req = requests.post(url, json=user)
    if req.status_code != 200:
        print(req.status_code)
    else:
        print("success")

# users = []
#
# for i in range(5):
#     req = requests.get(f'{url}?page={i}')
#     users += req.json()
#
# ids = []
# connection_check = {}
# for user in users:
#     ids.append(user['id'])
#     connection_check[user['id']] = False
#
# friend_list = {}
#
# for id in ids:
#     friends = generate_list(id, ids)
#     friend_list[id] = friends
#     for friend_id in friends:
#         if friend_id in friend_list.keys():
#             if id not in friend_list[friend_id]:
#                 friend_list[friend_id].append(id)
#
#
# connected = check_connection(connection_check, friend_list, list(friend_list.keys())[0])
#
# if connected:
#     with open('friends.json', 'w', encoding='utf-8') as f:
#         print(json.dumps(friend_list,indent=4),file=f)

# with open('friends.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# for key, value in data.items():
#     req = requests.put(f'{url}/{key}/friends', json=value)
#     if req.status_code == 200:
#         print('success')
#     else:
#         print(req.text)

# print(friend_list)
