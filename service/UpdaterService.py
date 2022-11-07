import json
from datetime import datetime

import dateutil
from dateutil import utils
import requests
from dateutil.parser import parse

from service.Persistence.PersistenceManager import PersistenceManager
from service.DataCleaner import DataCleaner


class UpdaterService:

    def __init__(self, last_modified_date=datetime.now()):
        self.last_modified_date = last_modified_date
        self.url = 'https://analisi.transparenciacatalunya.cat/resource/rhpv-yr4f.json'
        self.repo = PersistenceManager()
        self.cleaner = DataCleaner()

    def get_events(self, from_date=None, limit=5000):
        today = dateutil.utils.today()
        str_today = today.strftime('%Y-%m-%dT%H:%M:%S')
        if not from_date:
            req = requests.get(
                 f'{self.url}?$limit={limit}&$where=date_trunc_ymd(data_fi) >= date_trunc_ymd(\'{str_today}\')'
            )
            data = json.loads(req.text)
            date_modified = parse(req.headers.get('Last-Modified'))
            if date_modified.replace(tzinfo=None) <= self.last_modified_date:
                return None
            else:
                # self.last_modified_date = date_modified.replace(tzinfo=None)
                current = self.repo.get_current_data()
                cleaned_data = self.cleaner.clean_data(data)
                to_send = self.cleaner.filter_data_by(cleaned_data, current)
                return to_send
