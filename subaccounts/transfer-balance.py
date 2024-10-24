import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SUBACCOUNT_KEY = os.getenv("SUBACCOUNT_KEY")
AMOUNT = os.getenv("AMOUNT")

from vonage import Auth, Vonage
from vonage_subaccounts import Transfer, TransferRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = TransferRequest(from_=VONAGE_API_KEY, to=SUBACCOUNT_KEY, amount=AMOUNT)

transfer: Transfer = client.subaccounts.transfer_balance(request)

print(transfer)