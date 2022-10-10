from config.settings import DS_TO_S_KEY_MAPPING


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
        clean_data = []
        for record in data:
            temp_record = {}
            for i, field in enumerate(record.keys()):
                new_field = DS_TO_S_KEY_MAPPING[field]
                if 'tags' in field:
                    temp_record[new_field] = DataCleaner.treat_tags(record[field])
                else:
                    temp_record[new_field] = record[field]
            clean_data.append(temp_record)
        return clean_data

    @staticmethod
    def filter_data_by(new_data: list, old_data: list, fields: list) -> list:
        already_present = [(str(record['codi']), record['denominacio']) for record in old_data]
        to_return = [record for record in new_data if (record['codi'], record['denominacio']) not in already_present]
        return to_return
