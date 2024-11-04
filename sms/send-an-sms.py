import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME")
TO_NUMBER = os.getenv("TO_NUMBER")

from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

message = SmsMessage(
    to=TO_NUMBER,
    from_=VONAGE_BRAND_NAME,
    text="A text message sent using the Vonage SMS API.",
)

response: SmsResponse = client.sms.send(message)
print(response)
