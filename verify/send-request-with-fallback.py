import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

VERIFY_BRAND_NAME = os.environ.get("VERIFY_BRAND_NAME")
VERIFY_NUMBER = os.environ.get("VERIFY_NUMBER")
VERIFY_TO_EMAIL = os.environ.get("VERIFY_TO_EMAIL")
VERIFY_FROM_EMAIL = os.environ.get("VERIFY_FROM_EMAIL")

from vonage import Auth, Vonage
from vonage_verify import (
    EmailChannel,
    SilentAuthChannel,
    StartVerificationResponse,
    VerifyRequest,
)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=VERIFY_BRAND_NAME,
    workflow=[
        SilentAuthChannel(to=VERIFY_NUMBER),
        EmailChannel(to=VERIFY_TO_EMAIL, from_=VERIFY_FROM_EMAIL),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
