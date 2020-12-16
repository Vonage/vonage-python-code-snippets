import os
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')

import nexmo

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

result = client.get_balance()
print(f"{result['value']:0.2f} EUR")
