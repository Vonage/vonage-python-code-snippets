import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

BRAND_NAME = os.environ.get("BRAND_NAME")
TO_NUMBER = os.environ.get("TO_NUMBER")

from vonage import Auth, Vonage
from vonage_verify import StartVerificationResponse, VerifyRequest, VoiceChannel

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

verify_request = VerifyRequest(
    brand=BRAND_NAME,
    workflow=[
        VoiceChannel(to=TO_NUMBER),
    ],
)

response: StartVerificationResponse = client.verify.start_verification(verify_request)
pprint(response)
