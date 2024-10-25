import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SMS_CALLBACK_URL = os.getenv('SMS_CALLBACK_URL')

from vonage import Auth, Vonage
from vonage_account import SettingsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

settings: SettingsResponse = client.account.update_default_sms_webhook(
    mo_callback_url=SMS_CALLBACK_URL
)

print(settings)
