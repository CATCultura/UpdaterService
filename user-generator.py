import json
import random

noms = []
cognoms = []

with open("noms.txt", 'r', encoding='utf-8') as file:
    temp = file.readlines()
    for line in temp:
        noms.append(line.strip())

with open("cognoms.txt", 'r', encoding='utf-8') as file:
    temp = file.readlines()
    for line in temp:
        cognoms.append(line.strip().capitalize())

users = []

for i in range(100):
    user = {}
    name_idx = random.randint(0, len(noms)-1)
    name = noms[name_idx]
    surname_idx = random.randint(0, len(cognoms)-1)
    surname = cognoms[surname_idx]
    user['nameAndSurname'] = f'{name} {surname}'
    first = random.randint(2, max(len(name),2))
    second = random.randint(2, max(len(surname),2))
    username = f'{name[0:first]}{surname[0:second]}'
    user['username'] = username
    user['email'] = f'{username}@example.com'
    user['password'] = '1234'
    users.append(user)

with open('users.json', 'w', encoding='utf8') as file:
    print(json.dumps(users,indent=4), file=file)
