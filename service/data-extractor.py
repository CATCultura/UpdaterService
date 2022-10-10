from datetime import datetime

import dateutil
import pandas as pd
import unidecode as unidecode
from dateutil.parser import ParserError


def converter(date_time):
    try:
        return dateutil.parser.parse(date_time)
    except Exception:
        return dateutil.parser.parse('01/01/1900 12:00:00 AM')


df = pd.read_csv('../Agenda_cultural_de_Catalunya__per_localitzacions_.csv', low_memory=False)

rename = {}
for column in df.columns:
    temp_string = unidecode.unidecode(column)
    rename[column] = temp_string.replace(" ", "_").lower()
df.rename(columns=rename,inplace=True)

today = datetime.now()

df['data_fi'] = df['data_fi'].apply(converter)

new_df = df[df.data_fi > today]

with open('../test.csv', 'w', encoding='utf-8') as file:
    new_df.to_csv(file, index=False)

with open('../test.json', 'w', encoding='utf-8') as file:
    new_df.to_json(file, orient='split', indent=4, index=False)
