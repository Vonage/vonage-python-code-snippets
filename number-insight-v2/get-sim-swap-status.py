import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
INSIGHT_NUMBER = os.getenv('INSIGHT_NUMBER')

from vonage import Client

client = Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

insight_response = client.number_insight_v2.fraud_check(INSIGHT_NUMBER, 'sim_swap')
pprint(insight_response)
