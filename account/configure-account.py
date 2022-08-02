import os
from os.path import join, dirname
from pprint import pprint
import vonage
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SMS_CALLBACK_URL = os.getenv('SMS_CALLBACK_URL')

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

result = client.account.update_default_sms_webhook({'moCallBackUrl':SMS_CALLBACK_URL})
pprint(result)
