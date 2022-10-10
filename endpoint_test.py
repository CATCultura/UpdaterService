import json

import dateutil.utils
import requests

from dateutil.parser import parse

url = 'https://analisi.transparenciacatalunya.cat/resource/rhpv-yr4f.json'

today = dateutil.utils.today()
str_today = today.strftime('%Y-%m-%dT%H:%M:%S')

req = requests.get(url + '?$limit=5000&$where=date_trunc_ymd(data_fi) >= date_trunc_ymd(\'' + str_today + '\')')
json_data = json.loads(req.text)
headers = req.headers
date_modified = req.headers.get('Last-Modified')
print(date_modified)
dt = parse(date_modified)

if dt.replace(tzinfo=None) < today:
    print('Not worth it')
with open('result.json', 'w', encoding='utf-8') as file:
    print(json.dumps(json_data, indent=4), file=file)
