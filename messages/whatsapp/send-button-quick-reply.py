import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)
WHATSAPP_TEMPLATE_NAMESPACE = os.environ.get("WHATSAPP_TEMPLATE_NAMESPACE")
WHATSAPP_TEMPLATE_NAME = os.environ.get("WHATSAPP_TEMPLATE_NAME")
TO_NUMBER = os.environ.get("TO_NUMBER")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER")

from vonage import Auth, Vonage
from vonage_messages.models import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

message = WhatsappCustom(
    to=TO_NUMBER,
    from_=WHATSAPP_NUMBER,
    custom={
        "type": "template",
        "template": {
            "namespace": WHATSAPP_TEMPLATE_NAMESPACE,
            "name": WHATSAPP_TEMPLATE_NAME,
            "language": {"code": "en", "policy": "deterministic"},
            "components": [
                {"type": "header", "parameters": [{"type": "text", "text": "12/26"}]},
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": "*Ski Trip*"},
                        {"type": "text", "text": "2019-12-26"},
                        {"type": "text", "text": "*Squaw Valley Ski Resort, Tahoe*"},
                    ],
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": 0,
                    "parameters": [{"type": "payload", "payload": "Yes-Button-Payload"}],
                },
                {
                    "type": "button",
                    "sub_type": "quick_reply",
                    "index": 1,
                    "parameters": [{"type": "payload", "payload": "No-Button-Payload"}],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
