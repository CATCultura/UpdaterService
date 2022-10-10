import json


class PersistenceManager:

    def __init__(self, path: str = ""):
        self.path = path

    def get_current_data(self):
        data = {}
        with open(f'service/Persistence/current_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data


