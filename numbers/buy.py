import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_NUMBER = os.getenv("VONAGE_NUMBER")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")

import vonage

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

try:
    response = client.buy_number({"country": COUNTRY_CODE, "msisdn": VONAGE_NUMBER})
    print("Number purchased")
except Exception as exc:
    print("Error purchasing number", exc)
