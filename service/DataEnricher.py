import dateutil

from service.DataCleaner import DataCleaner
from service.RequestService import RequestService
from service.config.settings import DATE_QUERY


class DataEnricher:

    def __init__(self):
        self._endpoint_url = 'https://analisi.transparenciacatalunya.cat/resource/2n2k-gg9s.json'
        self.cleaner = DataCleaner()
        today = dateutil.utils.today()
        self.str_today = today.strftime('%Y-%m-%dT%H:%M:%S')

    def enrich_data(self, data):
        org_raw_data = RequestService.get_response(f'{self._endpoint_url}{DATE_QUERY.format(5000, self.str_today)}')
        org_cleaned_data = self.cleaner.clean_data(org_raw_data)

        org_map = {}
        for element in org_cleaned_data:
            pk = element['denominacio'] + element['dataInici']
            org_info = {}
            for key in element.keys():
                if 'Organitzador' in key:
                    org_info[key] = element[key]
            if pk in org_map.keys():
                org_map[pk] = {**org_map[pk], **org_info}
            else:
                org_map[pk] = org_info

        result = []
        for element in data:
            pk = element['denominacio'] + element['dataInici']
            if pk in org_map.keys():
                result.append({**element, **org_map[pk]})
        return result
