import json

import requests


class RequestService:

    @staticmethod
    def get_response(url: str) -> list:
        req = requests.get(
            url
        )
        data = json.loads(req.text)
        return data
