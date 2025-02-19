import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
MMS_SENDER_ID = os.environ.get("MMS_SENDER_ID")
MESSAGES_AUDIO_URL = os.environ.get("MESSAGES_AUDIO_URL")

from vonage import Auth, Vonage
from vonage_messages.models import MmsAudio, MmsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MmsAudio(
    to=MESSAGES_TO_NUMBER,
    from_=MMS_SENDER_ID,
    audio=MmsResource(url=MESSAGES_AUDIO_URL),
)

response = client.messages.send(message)
print(response)
