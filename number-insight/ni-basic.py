import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
INSIGHT_NUMBER = os.getenv('INSIGHT_NUMBER')

import vonage

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

insight_json = client.number_insight.get_basic_number_insight(number=INSIGHT_NUMBER)
pprint(insight_json)