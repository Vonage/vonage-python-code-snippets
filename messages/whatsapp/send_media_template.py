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

MEDIA_TEMPLATE = {
    "type": "template",
    "template": {
        "namespace": WHATSAPP_TEMPLATE_NAMESPACE,
        "name": WHATSAPP_TEMPLATE_NAME,
        "language": {"policy": "deterministic", "code": "en"},
        "components": [
            {
                "type": "header",
                "parameters": [
                    {
                        "type": "location",
                        "location": {
                            "longitude": -122.425332,
                            "latitude": 37.758056,
                            "name": "Facebook HQ",
                            "address": "1 Hacker Way, Menlo Park, CA 94025",
                        },
                    }
                ],
            },
            {
                "type": "body",
                "parameters": [
                    {"type": "text", "text": "Value 1"},
                    {"type": "text", "text": "Value 2"},
                    {"type": "text", "text": "Value 3"},
                ],
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
        "custom": MEDIA_TEMPLATE,
    }
)
