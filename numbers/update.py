import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_NUMBER = os.getenv("VONAGE_NUMBER")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
MESSAGES_APPLICATION_ID = os.getenv("MESSAGES_APPLICATION_ID")
VOICE_CALLBACK_TYPE = os.getenv("VOICE_CALLBACK_TYPE")
VOICE_CALLBACK_VALUE = os.getenv("VOICE_CALLBACK_VALUE")
VOICE_STATUS_URL = os.getenv("VOICE_STATUS_URL")
SMS_CALLBACK_URL = os.getenv("SMS_CALLBACK_URL")

import vonage

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

try:
    response = client.numbers.update_number(
        {
            "msisdn": VONAGE_NUMBER,
            "country": COUNTRY_CODE,
            "messagesCallbackType": "app",
            "messagesCallbackValue": MESSAGES_APPLICATION_ID,
            "voiceCallbackType": VOICE_CALLBACK_TYPE,
            "voiceCallbackValue": VOICE_CALLBACK_VALUE,
            "voiceStatusCallback": VOICE_STATUS_URL,
            "moHttpUrl": SMS_CALLBACK_URL,
        }
    )
    print("Number updated")
except Exception as exc:
    print("Error updating number", exc)
