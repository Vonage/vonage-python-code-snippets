import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
TO_NUMBER = os.getenv("TO_NUMBER")
PAYEE = os.environ.get("PAYEE")
AMOUNT = os.environ.get("AMOUNT")

from vonage import Auth, Vonage
from vonage_verify_legacy import StartVerificationResponse, Psd2Request

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = Psd2Request(number=TO_NUMBER, payee=PAYEE, amount=AMOUNT)

response: StartVerificationResponse = client.verify_legacy.start_psd2_verification(
    request
)
print(response)
