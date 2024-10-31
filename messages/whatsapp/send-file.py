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
FILE_URL = os.environ.get("FILE_URL")

from vonage import Auth, Vonage
from vonage_messages.models import WhatsappFile, WhatsappFileResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

message = WhatsappFile(
    to=TO_NUMBER,
    from_=WHATSAPP_NUMBER,
    file=WhatsappFileResource(url=FILE_URL, caption="Test file"),
)

response = client.messages.send(message)
print(response)
