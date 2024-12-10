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
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")
VIDEO_URL = os.environ.get("VIDEO_URL")

from vonage import Auth, Vonage
from vonage_messages.models import RcsVideo, RcsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

message = RcsVideo(
    to=TO_NUMBER,
    from_=RCS_SENDER_ID,
    video=RcsResource(url='VIDEO_URL'),
)

response = client.messages.send(message)
print(response)