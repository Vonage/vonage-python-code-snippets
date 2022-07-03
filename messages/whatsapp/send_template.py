import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

TO_NUMBER = os.environ.get("TO_NUMBER")
VONAGE_NUMBER = os.environ.get("FROM_NUMBER")

WHATSAPP_TEMPLATE_NAMESPACE = os.environ.get("WHATSAPP_TEMPLATE_NAMESPACE")
WHATSAPP_TEMPLATE_NAME = os.environ.get("WHATSAPP_TEMPLATE_NAME")

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.messages.send_message(
    {
        "channel": "whatsapp",
        "message_type": "template",
        "to": TO_NUMBER,
        "from": VONAGE_NUMBER,
        "template": {
            "name": f"{WHATSAPP_TEMPLATE_NAMESPACE}:{WHATSAPP_TEMPLATE_NAME}",
            "parameters": [
                {"default": "Vonage Verification"},
                {"default": "64873"},
                {"default": "10"},
            ],
        },
        "whatsapp": {"policy": "deterministic", "locale": "en-GB"},
    }
)
