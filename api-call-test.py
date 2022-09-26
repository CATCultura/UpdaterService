import pandas as pd
from sodapy import Socrata

api_key_id= '6leu2u5jknlvthd1t8iqyqeab'
api_secret_key = '1q9kvz2crlrewjyo7zthdw8s4cj0y8nwpv6f06egz2dwnicy4r'
app_token = 'bWRtKZKzi72eqCjSU6kWK9iSm'
client = Socrata('analisi.transparenciacatalunya.cat', app_token=app_token)

results = client.get("rhpv-yr4f",limit = 65000)
results_df = pd.DataFrame.from_records(results)
print(results_df.info())
