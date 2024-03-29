import json

import dateutil
from dateutil import utils
import requests

from service.DataCleaner import DataCleaner
from service.DataEnricher import DataEnricher

today = dateutil.utils.today()
str_today = today.strftime('%Y-%m-%dT%H:%M:%S')
url = 'https://analisi.transparenciacatalunya.cat/resource/2n2k-gg9s.json'
url_loc = 'https://analisi.transparenciacatalunya.cat/resource/rhpv-yr4f.json'
req = requests.get(
    f'{url_loc}?$limit=5000&$where=date_trunc_ymd(data_fi) >= date_trunc_ymd(\'{str_today}\')'
)
data = json.loads(req.text)
with open('../data/current_data.json', 'w', encoding='utf-8') as file:
    cleaned = DataCleaner.clean_data(data)
    enricher = DataEnricher()
    enriched_data = enricher.enrich_data(cleaned)
    print(json.dumps(enriched_data, indent=4), file=file)
