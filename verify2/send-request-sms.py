import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

BRAND_NAME = os.environ.get("BRAND_NAME")
TO_NUMBER = os.environ.get("TO_NUMBER")

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

params = {
    'brand': BRAND_NAME,
    'workflow': [
        {'channel': 'sms', 'to': TO_NUMBER},
    ],
}

client.verify2.new_request(params)
