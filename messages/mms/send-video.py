import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
MMS_SENDER_ID = os.environ.get("MMS_SENDER_ID")
MESSAGES_VIDEO_URL = os.environ.get("MESSAGES_VIDEO_URL")

from vonage import Auth, Vonage
from vonage_messages import MmsResource, MmsVideo

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MmsVideo(
    to=MESSAGES_TO_NUMBER,
    from_=MMS_SENDER_ID,
    video=MmsResource(url=MESSAGES_VIDEO_URL),
)

response = client.messages.send(message)
print(response)
