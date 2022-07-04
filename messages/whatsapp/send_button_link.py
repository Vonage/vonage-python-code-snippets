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
HEADER_IMAGE_URL = os.environ.get("HEADER_IMAGE_URL")

BUTTON = {
    "type": "template",
    "template": {
        "namespace": WHATSAPP_TEMPLATE_NAMESPACE,
        "name": WHATSAPP_TEMPLATE_NAME,
        "language": {"code": "en", "policy": "deterministic"},
        "components": [
            {
                "type": "header",
                "parameters": [{"type": "image", "image": {"link": HEADER_IMAGE_URL}}],
            },
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "Anand"},
                    {"type": "text", "text": "Quest"},
                    {"type": "text", "text": "113-0921387"},
                    {"type": "text", "text": "23rd Nov 2019"},
                ],
            },
            {
                "type": "button",
                "index": "0",
                "sub_type": "url",
                "parameters": [{"type": "text", "text": "1Z999AA10123456784"}],
            },
        ],
    },
}

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.messages.send_message(
    {
        "channel": "whatsapp",
        "message_type": "custom",
        "to": TO_NUMBER,
        "from": VONAGE_NUMBER,
        "custom": BUTTON,
    }
)
