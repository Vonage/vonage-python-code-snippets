import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")
MESSAGES_FILE_URL = os.environ.get("MESSAGES_FILE_URL")

from vonage import Auth, Vonage
from vonage_messages import RcsFile, RcsResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = RcsFile(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    file=RcsResource(url=MESSAGES_FILE_URL),
)

response = client.messages.send(message)
print(response)
