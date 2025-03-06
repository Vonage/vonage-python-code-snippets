import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VERIFY_REQUEST_ID = os.getenv("VERIFY_REQUEST_ID")

from vonage import Auth, Vonage

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

client.verify_legacy.cancel_verification(VERIFY_REQUEST_ID)
