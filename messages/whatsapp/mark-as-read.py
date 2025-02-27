import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
GEOSPECIFIC_MESSAGES_API_URL = os.environ.get("GEOSPECIFIC_MESSAGES_API_URL")
MESSAGES_MESSAGE_ID = os.environ.get("MESSAGES_MESSAGE_ID")

from vonage import Auth, HttpClientOptions, Vonage

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=GEOSPECIFIC_MESSAGES_API_URL),
)

client.messages.mark_whatsapp_message_read("MESSAGES_MESSAGE_ID")
