import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
VIBER_SENDER_ID = os.environ.get("VIBER_SENDER_ID")
MESSAGES_VIDEO_URL = os.environ.get("MESSAGES_VIDEO_URL")
MESSAGES_IMAGE_URL = os.environ.get("MESSAGES_IMAGE_URL")
MESSAGES_VIDEO_DURATION = os.environ.get("MESSAGES_VIDEO_DURATION")
MESSAGES_VIDEO_FILE_SIZE = os.environ.get("MESSAGES_VIDEO_FILE_SIZE")

from vonage import Auth, Vonage
from vonage_messages import ViberVideo, ViberVideoOptions, ViberVideoResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = ViberVideo(
    to=MESSAGES_TO_NUMBER,
    from_=VIBER_SENDER_ID,
    video=ViberVideoResource(url=MESSAGES_VIDEO_URL, thumb_url=MESSAGES_IMAGE_URL),
    viber_service=ViberVideoOptions(
        duration=MESSAGES_VIDEO_DURATION,
        file_size=MESSAGES_VIDEO_FILE_SIZE,
    ),
)

response = client.messages.send(message)
print(response)
