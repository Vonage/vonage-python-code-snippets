import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
MESSAGES_TO_NUMBER = os.getenv("MESSAGES_TO_NUMBER")
SMS_SENDER_ID = os.getenv("SMS_SENDER_ID")

from vonage import Auth, Vonage
from vonage_messages import Sms

client = Vonage(
    Auth(
        api_key=VONAGE_API_KEY,
        api_secret=VONAGE_API_SECRET,
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
