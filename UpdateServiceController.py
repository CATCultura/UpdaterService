import json
from datetime import date, datetime

import flask
import requests

from service.Persistence.PersistenceManager import PersistenceManager
from service.PersistenceService import PersistenceService
from service.UpdaterService import UpdaterService

url = 'http://10.4.41.41:8081/'

last_date = datetime.strptime('2022/10/9', '%Y/%m/%d')
updater_service = UpdaterService(last_date)

persistence_service = PersistenceService()
app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route("/update", methods=['GET'])
def update():
    data = updater_service.get_events()
    json_string = json.dumps(data, indent=4)
    persistence_service.save(data)
    # req = requests.post(f'{url}update-events')
    return json_string


@app.route("/get-all", methods=['GET'])
def get_all():
    data = PersistenceManager().get_current_data()
    return json.dumps(data, indent=4)


app.run(port=5001, host='0.0.0.0')
