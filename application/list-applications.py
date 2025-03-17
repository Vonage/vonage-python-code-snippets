import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

from vonage import Auth, Vonage
from vonage_application import ListApplicationsFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

applications, next_page = client.application.list_applications(
    filter=ListApplicationsFilter(page_size=10, page=1)
)

pprint(f'Applications:\n{applications}, \nNext page: {next_page}')
