import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
TO_NUMBER = os.environ.get("TO_NUMBER")
VIBER_SERVICE_MESSAGE_ID = os.environ.get("VIBER_SERVICE_MESSAGE_ID")
IMAGE_URL = os.environ.get("IMAGE_URL")

from vonage import Auth, Vonage
from vonage_messages import ViberImage, ViberImageResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = ViberImage(
    to=TO_NUMBER,
    from_=VIBER_SERVICE_MESSAGE_ID,
    image=ViberImageResource(url=IMAGE_URL),
)

response = client.messages.send(message)
print(response)
