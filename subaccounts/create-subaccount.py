import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
NEW_SUBACCOUNT_NAME = os.getenv('NEW_SUBACCOUNT_NAME')
NEW_SUBACCOUNT_SECRET = os.getenv('NEW_SUBACCOUNT_SECRET')

from vonage import Auth, Vonage
from vonage_subaccounts import NewSubaccount, SubaccountOptions

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: NewSubaccount = client.subaccounts.create_subaccount(
    SubaccountOptions(
        name=NEW_SUBACCOUNT_NAME,
        secret=NEW_SUBACCOUNT_SECRET,
        use_primary_account_balance=False,
    )
)

print(response)
