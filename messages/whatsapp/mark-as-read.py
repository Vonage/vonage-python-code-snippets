import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)
GEOSPECIFIC_VONAGE_API_HOST = os.environ.get("GEOSPECIFIC_VONAGE_API_HOST")
MESSAGE_UUID = os.environ.get("MESSAGE_UUID")

from vonage import Auth, HttpClientOptions, Vonage

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    ),
    http_client_options=HttpClientOptions(api_host=GEOSPECIFIC_VONAGE_API_HOST),
)

client.messages.mark_whatsapp_message_read("MESSAGE_UUID")
