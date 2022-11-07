from typing import Tuple

from service.config.settings import DS_TO_S_KEY_MAPPING, GEO_KEYS, REDUNDANT_KEYS


class DataCleaner:

    @staticmethod
    def treat_tags(tag_string: str) -> list:
        tags = tag_string.split(',')
        new_tags = []
        for tag in tags:
            new_tags.append(tag.split('/')[1])
        return new_tags

    @staticmethod
    def clean_data(data: list) -> list:
        cleaned_data = DataCleaner.clean_naming_and_formatting(data)
        return DataCleaner.sanitize_data(cleaned_data)

    @staticmethod
    def clean_naming_and_formatting(data):
        clean_data = []
        for record in data:
            temp_record = {}
            for i, field in enumerate(record.keys()):
                new_field = DS_TO_S_KEY_MAPPING[field]
                if 'tags' in field:
                    temp_record[new_field] = DataCleaner.treat_tags(record[field])
                elif 'imatges' in field:
                    temp_record[new_field] = record[field].split(',')
                elif 'comarca' in field:
                    temp_record[new_field] = DataCleaner.clean_location(record[field])
                else:
                    temp_record[new_field] = record[field]
            clean_data.append(temp_record)
        return clean_data

    @staticmethod
    def filter_data_by(new_data: list, old_data: list, fields: list) -> list:
        already_present = [(str(record['codi']), record['denominacio']) for record in old_data]
        to_return = [record for record in new_data if
                     (str(record['codi']), record['denominacio']) not in already_present]
        return to_return

    @staticmethod
    def clean_location(dirty):
        aux = dirty.split(':')[1]
        location = aux.split('/')
        location.reverse()
        result = ""
        for i in range(len(location) - 1):
            if i > 0:
                result += ', '
            new_loc = location[i].replace('-', ' ')

            result += f'{new_loc.title()}'
        return result

    @staticmethod
    def merge_geoinformation(dirty):
        result = {}
        if 'comarcaIMunicipi' in dirty.keys() and 'localitat' in dirty.keys():
            result, throwaway = DataCleaner.extract_remaining_information(dirty, ['comarcaIMunicipi', 'localitat'])
            result['ubicacio'] = f'{dirty["localitat"]} ({dirty["comarcaIMunicipi"]})'

        elif 'comarcaIMunicipi' in dirty.keys():
            result, throwaway = DataCleaner.extract_remaining_information(dirty, ['comarcaIMunicipi'])
            result['ubicacio'] = dirty['comarcaIMunicipi']

        elif 'regioOPais' in dirty.keys() and 'localitat' in dirty.keys():
            result, throwaway = DataCleaner.extract_remaining_information(dirty, ['regioOPais', 'localitat'])
            result['ubicacio'] = f'{dirty["localitat"]} ({dirty["regioOPais"]})'

        elif 'localitat' in dirty.keys():
            result, throwaway = DataCleaner.extract_remaining_information(dirty, ['localitat'])
            result['ubicacio'] = f'{dirty["localitat"]}'

        elif 'adreca' in dirty.keys():
            result = dirty
            result['ubicacio'] = 'Consulteu adreça'

        elif 'espai' in dirty.keys():
            result = dirty
            result['ubicacio'] = 'Vegeu espai'

        else:
            result['ubicacio'] = 'Activitat online'

        return result

    @staticmethod
    def extract_remaining_information(dirty: dict, keys: list) -> Tuple[dict, dict]:
        result = {}
        rem = {}
        result_keys = set(dirty.keys()).difference(set(keys))
        rem_keys = set(dirty.keys()).intersection(set(keys))
        for _key in result_keys:
            result[_key] = dirty[_key]

        for _key in rem_keys:
            rem[_key] = dirty[_key]

        return result, rem

    @staticmethod
    def sanitize_data(cleaned_data):
        final_data = []
        for data_piece in cleaned_data:
            for redundant_key in REDUNDANT_KEYS:
                data_piece.pop(redundant_key)
            res, rem = DataCleaner.extract_remaining_information(data_piece, GEO_KEYS)
            location_data = DataCleaner.merge_geoinformation(rem)
            final_data.append({**res, **location_data})

        return final_data

