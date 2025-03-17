import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
SMS_TO_NUMBER = os.getenv("SMS_TO_NUMBER")
SMS_SENDER_ID = os.getenv("SMS_SENDER_ID")
SMS_SIGNATURE = os.getenv('SMS_SIGNATURE')

from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, signature_secret=SMS_SIGNATURE))

message = SmsMessage(
    to=SMS_TO_NUMBER,
    from_=SMS_SENDER_ID,
    text="A text message sent using the Vonage SMS API.",
)

response: SmsResponse = client.sms.send(message)
print(response)
