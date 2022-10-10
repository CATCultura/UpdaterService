import json
from datetime import date, datetime

import flask

from service.UpdaterService import UpdaterService

# last_date = datetime.strptime('2022/10/9', '%Y/%m/%d')
updater_service = UpdaterService(last_date)
app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route("/update", methods=['GET'])
def update():
    data = updater_service.get_events()
    json_string = json.dumps(data, indent=4)
    return json_string


app.run(port=5001)
