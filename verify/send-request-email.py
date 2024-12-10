import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)

BRAND_NAME = os.environ.get("BRAND_NAME")
TO_EMAIL = os.environ.get("TO_EMAIL")

from vonage import Auth, Vonage
from vonage_verify import EmailChannel, StartVerificationResponse, VerifyRequest

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

verify_request = VerifyRequest(
    brand=BRAND_NAME,
    workflow=[
        EmailChannel(to=TO_EMAIL),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)