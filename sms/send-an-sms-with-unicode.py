import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SMS_TO_NUMBER = os.getenv("SMS_TO_NUMBER")
SMS_SENDER_ID = os.getenv("SMS_SENDER_ID")

from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

message = SmsMessage(
    to=SMS_TO_NUMBER,
    from_=SMS_SENDER_ID,
    text='こんにちは世界',
    type='unicode',
)

response: SmsResponse = client.sms.send(message)
print(response)
