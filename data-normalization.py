import json
from datetime import datetime

import dateutil
import pandas as pd


def converter(date_time):
    if type(date_time) is int:
        try:
            return datetime.utcfromtimestamp(date_time / 1000)
        except:
            return dateutil.parser.parse('01/01/1900 12:00:00 AM')
    else:
        try:
            return dateutil.parser.parse(date_time)
        except Exception:
            return dateutil.parser.parse('01/01/1900 12:00:00 AM')


file = open('test.json', 'r', encoding='utf-8')
data = json.load(file)

headers = data['columns']
clean_data = []
for j, record in enumerate(data['data']):
    temp_record = {}
    for i, column in enumerate(headers):
        if "data" in column:
            temp_record[column] = str(converter(record[i]))

        elif 'tags' in column:
            if record[i] is not None:
                tags = record[i].split(',')
                new_tags = []
                for tag in tags:
                    new_tags.append(tag.split('/')[1])
                temp_record[column] = new_tags
            else:
                temp_record[column] = None
        else:
            temp_record[column] = record[i]
    clean_data.append(temp_record)


with open('cleaned_data.json', 'w', encoding='ascii') as file:
    info = json.dumps(clean_data, indent=4)
    print(info, file=file)
