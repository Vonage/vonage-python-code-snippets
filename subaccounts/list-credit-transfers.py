import os
from os.path import dirname, join

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SUBACCOUNT_START_DATE = os.getenv("SUBACCOUNT_START_DATE")

from vonage import Auth, Vonage
from vonage_subaccounts import ListTransfersFilter, Transfer

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: list[Transfer] = client.subaccounts.list_credit_transfers(
    ListTransfersFilter(start_date=SUBACCOUNT_START_DATE)
)

print(response)
