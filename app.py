from urllib.request import urlopen
import json
import pandas as pd

response = urlopen('https://api.openf1.org/v1/car_data?driver_number=55&session_key=9159&speed>=315')
data = json.loads(response.read().decode('utf-8'))

df = pd.DataFrame(data)

print(df)