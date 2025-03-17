import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")
ACCOUNT_SECRET_ID = os.environ.get("ACCOUNT_SECRET_ID")

from vonage import Auth, Vonage
from vonage_account import VonageApiSecret

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

secret: VonageApiSecret = client.account.get_secret(ACCOUNT_SECRET_ID)

print(f'Secret ID: {secret.id}; Created at {secret.created_at}')
