import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")
WHATSAPP_STICKER_URL = os.environ.get("WHATSAPP_STICKER_URL")

from vonage import Auth, Vonage
from vonage_messages import WhatsappSticker, WhatsappStickerUrl

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappSticker(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    sticker=WhatsappStickerUrl(url=WHATSAPP_STICKER_URL),
)

response = client.messages.send(message)
print(response)
