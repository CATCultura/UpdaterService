import json
import os


class PersistenceManager:

    def __init__(self, path: str = ""):
        if not path:
            temp = f'{os.getcwd()}{os.sep}data{os.sep}'
            self.path = temp
        else:
            self.path = path

    def get_current_data(self):
        data = {}
        with open(f'{self.path}current_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

    def save(self, data: list):
        c_data = self.get_current_data()
        new_data = c_data + data
        with open(f'{self.path}current_data.json', 'w', encoding='utf-8') as file:
            print(json.dumps(new_data), file=file)
