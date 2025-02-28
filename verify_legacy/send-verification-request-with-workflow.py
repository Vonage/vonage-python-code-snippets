import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
TO_NUMBER = os.getenv("TO_NUMBER")
WORKFLOW_ID = os.environ.get("WORKFLOW_ID")

from vonage import Auth, Vonage
from vonage_verify_legacy import StartVerificationResponse, VerifyRequest

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

request = VerifyRequest(number=TO_NUMBER, brand='AcmeInc', workflow_id=WORKFLOW_ID)

response: StartVerificationResponse = client.verify_legacy.start_verification(request)
print(response)
