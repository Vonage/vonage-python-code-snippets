import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)
TO_NUMBER = os.environ.get("TO_NUMBER")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER")
WHATSAPP_AUTH_TEMPLATE_NAME = os.environ.get("WHATSAPP_AUTH_TEMPLATE_NAME")

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
            "name": WHATSAPP_AUTH_TEMPLATE_NAME,
            "language": {"policy": "deterministic", "code": "en"},
            "components": [
                {"type": "body", "parameters": [{"type": "text", "text": "'$OTP'"}]},
                {
                    "type": "button",
                    "sub_type": "url",
                    "index": "0",
                    "parameters": [{"type": "text", "text": "'$OTP'"}],
                },
            ],
        },
    },
)

response = client.messages.send(message)
print(response)
