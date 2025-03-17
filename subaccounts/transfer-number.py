import os
from os.path import dirname, join

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SUBACCOUNT_KEY = os.getenv("SUBACCOUNT_KEY")
VONAGE_VIRTUAL_NUMBER = os.getenv("VONAGE_VIRTUAL_NUMBER")

from vonage import Auth, Vonage
from vonage_subaccounts import TransferNumberRequest, TransferNumberResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = TransferNumberRequest(
    from_=VONAGE_API_KEY, to=SUBACCOUNT_KEY, number=VONAGE_VIRTUAL_NUMBER
)

response: TransferNumberResponse = client.subaccounts.transfer_number(request)

print(response)
