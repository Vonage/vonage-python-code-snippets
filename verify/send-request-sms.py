import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

VERIFY_BRAND_NAME = os.environ.get("VERIFY_BRAND_NAME")
VERIFY_NUMBER = os.environ.get("VERIFY_NUMBER")

from vonage import Auth, Vonage
from vonage_verify import SmsChannel, StartVerificationResponse, VerifyRequest

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        SmsChannel(to=VERIFY_NUMBER),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
