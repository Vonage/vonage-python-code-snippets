import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
WHATSAPP_TEMPLATE_NAMESPACE = os.environ.get("WHATSAPP_TEMPLATE_NAMESPACE")
WHATSAPP_TEMPLATE_NAME = os.environ.get("WHATSAPP_TEMPLATE_NAME")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")

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
