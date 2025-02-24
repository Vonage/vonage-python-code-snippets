import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")
WHATSAPP_TEMPLATE_NAME = os.environ.get("WHATSAPP_TEMPLATE_NAME")
IMAGE_URL = os.environ.get("IMAGE_URL")
WHATSAPP_TEMPLATE_REPLACEMENT_TEXT = os.environ.get("WHATSAPP_TEMPLATE_REPLACEMENT_TEXT")

from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        "type": "template",
        "template": {
            "name": WHATSAPP_TEMPLATE_NAME,
            "language": {"policy": "deterministic", "code": "en"},
            "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": IMAGE_URL,
                            },
                        },
                    ],
                },
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": WHATSAPP_TEMPLATE_REPLACEMENT_TEXT}
                    ],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
