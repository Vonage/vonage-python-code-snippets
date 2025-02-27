import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSAGES_SANDBOX_HOST = os.environ.get("MESSAGES_SANDBOX_HOST")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import WhatsappText

client = Vonage(
    auth=Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host=MESSAGES_SANDBOX_HOST),
)

message = WhatsappText(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    text="This is a WhatsApp text message sent using the Vonage Messages API via the Messages Sandbox",
)

response = client.messages.send(message)
print(response)
