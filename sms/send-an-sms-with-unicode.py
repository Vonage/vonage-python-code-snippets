import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
TO_NUMBER = os.getenv("TO_NUMBER")

from vonage import Client, Sms

sms = Sms(Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET))

sms.send_message(
    {"from": "Acme Inc", "to": TO_NUMBER, "text": "こんにちは世界", "type": "unicode",}
)
