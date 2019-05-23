import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")
NEXMO_NUMBER = os.getenv("NEXMO_NUMBER")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
MESSAGES_APPLICATION_ID = os.getenv("MESSAGES_APPLICATION_ID")
VOICE_CALLBACK_TYPE = os.getenv("VOICE_CALLBACK_TYPE")
VOICE_CALLBACK_VALUE = os.getenv("VOICE_CALLBACK_VALUE")
VOICE_STATUS_URL = os.getenv("VOICE_STATUS_URL")
SMS_CALLBACK_URL = os.getenv("SMS_CALLBACK_URL")

import nexmo

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

try:
    response = client.update_number(
        {
            "msisdn": NEXMO_NUMBER,
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
