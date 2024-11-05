import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)
VONAGE_BRAND_NAME = os.environ.get("VONAGE_BRAND_NAME")
TO_NUMBER = os.environ.get("TO_NUMBER")

from vonage import Auth, Vonage
from vonage_messages.models import Sms

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

response = client.messages.send(
    Sms(
        to=TO_NUMBER,
        from_=VONAGE_BRAND_NAME,
        text='This is an SMS sent using the Vonage Messages API.',
    )
)
print(response)
