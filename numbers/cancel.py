import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")
NEXMO_NUMBER = os.getenv("NEXMO_NUMBER")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")

import nexmo

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

try:
    response = client.cancel_number({"country": COUNTRY_CODE, "msisdn": NEXMO_NUMBER})
    print("Number cancelled")
except Exception as exc:
    print("Error cancelling number", exc)
