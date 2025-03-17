import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")
MESSAGES_AUDIO_URL = os.environ.get("MESSAGES_AUDIO_URL")

from vonage import Auth, HttpClientOptions, Vonage
from vonage_messages import WhatsappAudio, WhatsappAudioResource

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    ),
    http_client_options=HttpClientOptions(api_host='messages-sandbox.nexmo.com'),
)

message = WhatsappAudio(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    audio=WhatsappAudioResource(url=MESSAGES_AUDIO_URL, caption="Test audio file"),
)

response = client.messages.send(message)
print(response)
