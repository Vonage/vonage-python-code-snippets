import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
REQUEST_ID = os.getenv("REQUEST_ID")
CODE = os.environ.get('CODE')

from vonage import Auth, Vonage
from vonage_verify_legacy import CheckCodeResponse

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

response: CheckCodeResponse = client.verify_legacy.check_code(REQUEST_ID, CODE)
print(response)
