import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VONAGE_NUMBER = os.getenv("VONAGE_NUMBER")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")

from vonage import Auth, Vonage
from vonage_numbers import NumberParams, NumbersStatus

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

status: NumbersStatus = client.numbers.buy_number(
    params=NumberParams(
        country=COUNTRY_CODE,
        msisdn=VONAGE_NUMBER,
    )
)

print(status.model_dump())
