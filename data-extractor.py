from datetime import datetime

import dateutil
import pandas as pd
from dateutil.parser import ParserError


def converter(date_time):
    try:
        return dateutil.parser.parse(date_time)
    except Exception:
        return dateutil.parser.parse('01/01/1900 12:00:00 AM')


df = pd.read_csv('Agenda_cultural_de_Catalunya__per_localitzacions_.csv', low_memory=False)

today = datetime.now()
df = df.rename({'Data fi': 'Dataf'}, axis=1, errors='raise')

df['Dataf'] = df['Dataf'].apply(converter)

new_df = df[df.Dataf > today]

with open('test.csv', 'w', encoding='utf-8') as file:
    new_df.to_csv(file, index=False)

with open('test.json', 'w', encoding='utf-8') as file:
    new_df.to_json(file,orient='split', indent=4, index=False)
