import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

client.sms.submit_sms_conversion(
    message_id='MESSAGE_ID',
    delivered=True,
    timestamp='2020-01-01T12:00:00Z',
)

if client.http_client.last_response.status_code == 200:
    print('Conversion submitted successfully.')
else:
    print('Conversion not submitted.')
