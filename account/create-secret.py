import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
NEW_SECRET = os.getenv('NEW_SECRET')

from vonage import Auth, Vonage
from vonage_account import VonageApiSecret

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: VonageApiSecret = client.account.create_secret(NEW_SECRET)
print(response)
