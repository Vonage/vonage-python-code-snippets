import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

from vonage import Auth, Vonage
from vonage_account import Balance

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

balance: Balance = client.account.get_balance()

print(f'{balance.value:0.2f} EUR, auto-reload: {balance.auto_reload}')
