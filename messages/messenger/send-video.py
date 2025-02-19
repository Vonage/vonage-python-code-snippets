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
VIDEO_URL = os.environ.get("VIDEO_URL")

from vonage import Auth, Vonage
from vonage_messages.models import MessengerVideo, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY_PATH,
    )
)VONAGE_PRIVATE_KEY

message = MessengerVideo(
    to=FB_RECIPIENT_ID,
    from_=VONAGE_FB_SENDER_ID,
    video=MessengerResource(url=VIDEO_URL),
)

response = client.messages.send(message)
print(response)
