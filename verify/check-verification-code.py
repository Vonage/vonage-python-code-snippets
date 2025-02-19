import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

REQUEST_ID = os.environ.get('REQUEST_ID')
CODE = os.environ.get('CODE')

from vonage import Auth, Vonage
from vonage_verify import CheckCodeResponse

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CheckCodeResponse = client.verify.check_code(request_id=REQUEST_ID, code=CODE)
print(response)
