import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
GEOSPECIFIC_VONAGE_API_HOST = os.environ.get("GEOSPECIFIC_VONAGE_API_HOST")
MESSAGES_MESSAGE_ID = os.environ.get("MESSAGES_MESSAGE_ID")

from vonage import Auth, Vonage

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.messages.revoke_rcs_message(MESSAGES_MESSAGE_ID)
print(response)
