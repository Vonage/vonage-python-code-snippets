import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSENGER_RECIPIENT_ID = os.environ.get("MESSENGER_RECIPIENT_ID")
MESSENGER_SENDER_ID = os.environ.get("MESSENGER_SENDER_ID")

from vonage import Auth, Vonage
from vonage_messages import MessengerText

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = MessengerText(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    text='Hello from the Vonage Messages API.',
)
try:
    response = client.messages.send(message)
    print(response)
except Exception as e:
    print(e)
    print(client.http_client.last_request.url)
