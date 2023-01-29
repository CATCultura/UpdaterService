import json
from base64 import b64encode
from datetime import date, datetime

import flask
import requests
from flask import request

from service.Persistence.PersistenceManager import PersistenceManager
from service.PersistenceService import PersistenceService
from service.UpdaterService import UpdaterService

# insert urls
remote_url = '**************'
remote_azure_url = '***********'

last_date = datetime.strptime('2022/10/9', '%Y/%m/%d')
updater_service = UpdaterService(last_date)

persistence_service = PersistenceService()
app = flask.Flask(__name__)
app.config['DEBUG'] = True


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'


@app.route("/update", methods=['GET'])
def update():
    data = updater_service.get_events()
    json_string = json.dumps(data, indent=4)
    args = request.args.to_dict()
    save = True if args.get('save') == 'true' else False
    update_db = True if args.get('update') == 'true' else False
    if save:
        persistence_service.save(data)
    if update_db:
        headers = {
            'Authorization': basic_auth('admin', 'admin')
        }
        req = requests.post(f'{remote_url}insert', json=data, headers=headers)
        req2 = requests.post(f'{remote_azure_url}insert', json=data, headers=headers)

    return json_string


@app.route("/get-all", methods=['GET'])
def get_all():
    data = PersistenceManager().get_current_data()
    return json.dumps(data, indent=4)


app.run(port=5001, host='0.0.0.0')
