import os
from os.path import join, dirname
from dotenv import load_dotenv
import vonage

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

result = client.account.get_balance()
print(f"{result['value']:0.2f} EUR")
