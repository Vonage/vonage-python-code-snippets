import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

from vonage import Auth, Vonage
from vonage_subaccounts import ListSubaccountsResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: ListSubaccountsResponse = client.subaccounts.list_subaccounts()

print(response)
