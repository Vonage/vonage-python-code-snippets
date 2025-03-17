import os
from os.path import dirname, join

from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
ACCOUNT_SECRET = os.getenv('ACCOUNT_SECRET')

from vonage import Auth, Vonage
from vonage_account import VonageApiSecret

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: VonageApiSecret = client.account.create_secret(ACCOUNT_SECRET)
print(response)
