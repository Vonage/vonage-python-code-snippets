import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
VONAGE_PRIVATE_KEY
VONAGE_FB_SENDER_ID = os.environ.get("VONAGE_FB_SENDER_ID")
FB_RECIPIENT_ID = os.environ.get("FB_RECIPIENT_ID")
IMAGE_URL = os.environ.get("IMAGE_URL")

from vonage import Auth, Vonage
from vonage_messages.models import MessengerImage, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)VONAGE_PRIVATE_KEY

message = MessengerImage(
    to=FB_RECIPIENT_ID,
    from_=VONAGE_FB_SENDER_ID,
    image=MessengerResource(url=IMAGE_URL),
)

response = client.messages.send(message)
print(response)
