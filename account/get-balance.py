import os
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint #Data pretty printer
import vonage

#Load_env
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

#get_api
VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')


#loading_model
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

#print_result
result = client.get_balance()
print(f"{result['value']:0.2f} EUR")
