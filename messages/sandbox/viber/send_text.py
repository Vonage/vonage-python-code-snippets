import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)

MESSAGES_SANDBOX_URL = os.environ.get("MESSAGES_SANDBOX_URL")
MESSAGES_SANDBOX_VIBER_SERVICE_ID = os.environ.get("MESSAGES_SANDBOX_VIBER_SERVICE_ID")
MESSAGES_SANDBOX_ALLOW_LISTED_TO_NUMBER = os.environ.get(
    "MESSAGES_SANDBOX_ALLOW_LISTED_TO_NUMBER"
)

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages.models import ViberText

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    ),
    http_client_options=HttpClientOptions(api_host=MESSAGES_SANDBOX_URL),
)

message = ViberText(
    to=MESSAGES_SANDBOX_ALLOW_LISTED_TO_NUMBER,
    from_=MESSAGES_SANDBOX_VIBER_SERVICE_ID,
    text="This is a Viber Service Message text message sent using the Messages API via the Messages Sandbox",
)

response = client.messages.send(message)
print(response)
