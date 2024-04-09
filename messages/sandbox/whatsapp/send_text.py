import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

MESSAGES_SANDBOX_URL = os.environ.get("MESSAGES_SANDBOX_URL")
MESSAGES_SANDBOX_WHATSAPP_NUMBER = os.environ.get("MESSAGES_SANDBOX_WHATSAPP_NUMBER")
MESSAGES_SANDBOX_ALLOW_LISTED_TO_NUMBER = os.environ.get("MESSAGES_SANDBOX_ALLOW_LISTED_TO_NUMBER")

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.api_host(MESSAGES_SANDBOX_URL)

client.messages.send_message(
    {
        "channel": "whatsapp",
        "message_type": "text",
        "to": MESSAGES_SANDBOX_ALLOW_LISTED_TO_NUMBER,
        "from": MESSAGES_SANDBOX_WHATSAPP_NUMBER,
        "text": "This is a WhatsApp text message sent using the Vonage Messages API via the Messages Sandbox",
    }
)
