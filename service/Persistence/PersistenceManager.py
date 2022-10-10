import json
import os


class PersistenceManager:

    def __init__(self, path: str = ""):
        if not path:
            temp = f'{os.getcwd()}{os.sep}service{os.sep}Persistence{os.sep}'
            self.path = temp
        else:
            self.path = path

    def get_current_data(self):
        data = {}
        with open(f'{self.path}current_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data
