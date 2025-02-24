import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")

MESSENGER_RECIPIENT_ID = os.environ.get("MESSENGER_RECIPIENT_ID")
MESSENGER_SENDER_ID = os.environ.get("MESSENGER_SENDER_ID")
MESSAGES_AUDIO_URL = os.environ.get("MESSAGES_AUDIO_URL")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import MessengerAudio, MessengerResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host='messages-sandbox.nexmo.com'),
)

message = MessengerAudio(
    to=MESSENGER_RECIPIENT_ID,
    from_=MESSENGER_SENDER_ID,
    audio=MessengerResource(url=MESSAGES_AUDIO_URL),
)

response = client.messages.send(message)
print(response)
