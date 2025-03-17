import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
SMS_SENDER_ID = os.environ.get("SMS_SENDER_ID")

from vonage import Auth, Vonage
from vonage_messages import Sms

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.messages.send(
    Sms(
        to=MESSAGES_TO_NUMBER,
        from_=SMS_SENDER_ID,
        text='This is an SMS sent using the Vonage Messages API.',
    )
)
print(response)
