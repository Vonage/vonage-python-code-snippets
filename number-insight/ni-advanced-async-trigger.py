import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
INSIGHT_NUMBER = os.getenv('INSIGHT_NUMBER')
INSIGHT_CALLBACK_URL = os.getenv('INSIGHT_CALLBACK_URL')

from vonage import Auth, Vonage
from vonage_number_insight import (AdvancedAsyncInsightRequest,
                                   AdvancedAsyncInsightResponse)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

insight: AdvancedAsyncInsightResponse = client.number_insight.get_advanced_info_async(
    AdvancedAsyncInsightRequest(number=INSIGHT_NUMBER, callback=INSIGHT_CALLBACK_URL)
)
pprint(insight)
