import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
TO_NUMBER = os.environ.get("TO_NUMBER")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER")
STICKER_URL = os.environ.get("STICKER_URL")

from vonage import Auth, Vonage
from vonage_messages.models import WhatsappSticker, WhatsappStickerUrl

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappSticker(
    to=TO_NUMBER,
    from_=WHATSAPP_NUMBER,
    sticker=WhatsappStickerUrl(url=STICKER_URL),
)

response = client.messages.send(message)
print(response)
