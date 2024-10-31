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
WHATSAPP_TEMPLATE_NAMESPACE = os.environ.get("WHATSAPP_TEMPLATE_NAMESPACE")
WHATSAPP_TEMPLATE_NAME = os.environ.get("WHATSAPP_TEMPLATE_NAME")

from vonage import Auth, Vonage
from vonage_messages.models import (
    WhatsappTemplate,
    WhatsappTemplateResource,
    WhatsappTemplateSettings,
)

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

message = WhatsappTemplate(
    to=TO_NUMBER,
    from_=WHATSAPP_NUMBER,
    template=WhatsappTemplateResource(
        name=f'{WHATSAPP_TEMPLATE_NAMESPACE}:{WHATSAPP_TEMPLATE_NAME}',
        parameters=["Vonage Verification", "64873", "10"],
    ),
    whatsapp=WhatsappTemplateSettings(
        locale="en-GB",
        policy="deterministic",
    ),
)

response = client.messages.send(message)
print(response)
