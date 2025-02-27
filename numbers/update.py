import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
NUMBER_COUNTRY_CODE = os.getenv("NUMBER_COUNTRY_CODE")
NUMBER_MSISDN = os.getenv("NUMBER_MSISDN")
NUMBER_SMS_CALLBACK_URL = os.getenv("NUMBER_SMS_CALLBACK_URL")
NUMBER_VOICE_CALLBACK_URL = os.getenv("NUMBER_VOICE_CALLBACK_URL")
NUMBER_VOICE_STATUS_CALLBACK_URL = os.getenv("NUMBER_VOICE_STATUS_CALLBACK_URL")

from vonage import Auth, Vonage
from vonage_numbers import NumbersStatus, UpdateNumberParams

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

status: NumbersStatus = client.numbers.update_number(
    UpdateNumberParams(
        country=NUMBER_COUNTRY_CODE,
        msisdn=NUMBER_MSISDN,
        app_id='vonage-application-id',
        mo_http_url=NUMBER_SMS_CALLBACK_URL,
        mo_smpp_sytem_type='inbound',
        voice_callback_value=NUMBER_VOICE_CALLBACK_URL,
        voice_status_callback=NUMBER_VOICE_STATUS_CALLBACK_URL,
    )
)

print(status.model_dump())
