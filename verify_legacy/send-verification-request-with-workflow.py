import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
VERIFY_NUMBER = os.getenv("VERIFY_NUMBER")
VERIFY_WORKFLOW_ID = os.environ.get("VERIFY_WORKFLOW_ID")

from vonage import Auth, Vonage
from vonage_verify_legacy import StartVerificationResponse, VerifyRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = VerifyRequest(
    number=VERIFY_NUMBER, brand='AcmeInc', workflow_id=VERIFY_WORKFLOW_ID
)

response: StartVerificationResponse = client.verify_legacy.start_verification(request)
print(response)
