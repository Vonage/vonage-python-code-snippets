import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VERIFY_REQUEST_ID = os.getenv("VERIFY_REQUEST_ID")

from vonage import Auth, Vonage
from vonage_verify_legacy import VerifyControlStatus

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: VerifyControlStatus = client.verify_legacy.trigger_next_event(VERIFY_REQUEST_ID)
print(response)
