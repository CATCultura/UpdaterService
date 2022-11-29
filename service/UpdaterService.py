import json
from datetime import datetime

import dateutil
from dateutil import utils
import requests
from dateutil.parser import parse

from service.DataEnricher import DataEnricher
from service.Persistence.PersistenceManager import PersistenceManager
from service.DataCleaner import DataCleaner
from service.RequestService import RequestService
from service.config.settings import DATE_QUERY


class UpdaterService:

    def __init__(self, last_modified_date=datetime.now()):
        self.last_modified_date = last_modified_date
        self.url = 'https://analisi.transparenciacatalunya.cat/resource/rhpv-yr4f.json'
        self.repo = PersistenceManager()
        self.cleaner = DataCleaner()
        self.enricher = DataEnricher()

    def get_events(self, from_date=None, limit=5000):
        today = dateutil.utils.today()
        str_today = today.strftime('%Y-%m-%dT%H:%M:%S')
        if not from_date:
            data = RequestService.get_response(f'{self.url}{DATE_QUERY.format(limit, str_today)}')
            current = self.repo.get_current_data()
            cleaned_data = self.cleaner.clean_data(data)
            enriched_data = self.enricher.enrich_data(cleaned_data)
            to_send = self.cleaner.filter_data_by(enriched_data, current)
            return to_send
