import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_NUMBER = os.getenv("VONAGE_NUMBER")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
VOICE_CALLBACK_TYPE = os.getenv("VOICE_CALLBACK_TYPE")
VOICE_CALLBACK_VALUE = os.getenv("VOICE_CALLBACK_VALUE")
VOICE_STATUS_URL = os.getenv("VOICE_STATUS_URL")
SMS_CALLBACK_URL = os.getenv("SMS_CALLBACK_URL")

from vonage import Auth, Vonage
from vonage_numbers import NumbersStatus, UpdateNumberParams

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

status: NumbersStatus = client.numbers.update_number(
    UpdateNumberParams(
        country=COUNTRY_CODE,
        msisdn=VONAGE_NUMBER,
        app_id='vonage-application-id',
        mo_http_url=SMS_CALLBACK_URL,
        mo_smpp_sytem_type='inbound',
        voice_callback_type=VOICE_CALLBACK_TYPE,
        voice_callback_value=VOICE_CALLBACK_VALUE,
        voice_status_callback=VOICE_STATUS_URL,
    )
)

print(status.model_dump())
