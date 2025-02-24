import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")
MESSAGES_IMAGE_URL = os.environ.get("MESSAGES_IMAGE_URL")

from vonage import Auth, Vonage
from vonage_messages import RcsImage, RcsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = RcsImage(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    image=RcsResource(url=MESSAGES_IMAGE_URL),
)

response = client.messages.send(message)
print(response)
