import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSAGES_SANDBOX_URL = os.environ.get("MESSAGES_SANDBOX_URL")
MESSAGES_SANDBOX_FB_ID = os.environ.get("MESSAGES_SANDBOX_FB_ID")
MESSAGES_SANDBOX_ALLOW_LISTED_FB_RECIPIENT_ID = os.environ.get(
    "MESSAGES_SANDBOX_ALLOW_LISTED_FB_RECIPIENT_ID"
)

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages.models import MessengerText

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=MESSAGES_SANDBOX_URL),
)

message = MessengerText(
    to=MESSAGES_SANDBOX_ALLOW_LISTED_FB_RECIPIENT_ID,
    from_=MESSAGES_SANDBOX_FB_ID,
    text="This is a Facebook Messenger text message sent using the Vonage Messages API via the Messages Sandbox",
)

response = client.messages.send(message)
print(response)
