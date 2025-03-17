import os
from os.path import dirname, join

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
SUBACCOUNT_KEY = os.getenv("SUBACCOUNT_KEY")

from vonage import Auth, Vonage
from vonage_subaccounts import ModifySubaccountOptions, Subaccount

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: Subaccount = client.subaccounts.modify_subaccount(
    subaccount_api_key=SUBACCOUNT_KEY,
    options=ModifySubaccountOptions(suspended=True),
)

print(response)
