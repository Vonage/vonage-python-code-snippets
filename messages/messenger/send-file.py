import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSENGER_RECIPIENT_ID = os.environ.get("MESSENGER_RECIPIENT_ID")
MESSENGER_SENDER_ID = os.environ.get("MESSENGER_SENDER_ID")
MESSAGES_FILE_URL = os.environ.get("MESSAGES_FILE_URL")

from vonage import Auth, Vonage
from vonage_messages import MessengerFile, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerFile(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    file=MessengerResource(url=MESSAGES_FILE_URL),
)

response = client.messages.send(message)
print(response)
