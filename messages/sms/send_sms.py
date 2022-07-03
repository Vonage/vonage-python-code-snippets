import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

VONAGE_BRAND_NAME = os.environ.get("VONAGE_BRAND_NAME")
TO_NUMBER = os.environ.get("TO_NUMBER")

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.messages.send_message(
    {
        "channel": "sms",
        "message_type": "text",
        "to": TO_NUMBER,
        "from": VONAGE_BRAND_NAME,
        "text": "This is an SMS sent using the Vonage Messages API",
    }
)
