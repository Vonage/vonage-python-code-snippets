import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import AudioConnectorData, AudioConnectorOptions, AudioConnectorWebSocket

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_SESSION_ID = os.getenv("VIDEO_SESSION_ID")
VIDEO_TOKEN = os.getenv("VIDEO_TOKEN")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

options = AudioConnectorOptions(
    session_id=VIDEO_SESSION_ID,
    token=VIDEO_TOKEN,
    websocket=AudioConnectorWebSocket(
        uri='wss://example.com/websocket', audio_rate=16000
    ),
)
audio_connector: AudioConnectorData = vonage_client.video.start_audio_connector(
    options)

print("=== Started AudioConnector ===")
print(json.dumps(audio_connector.model_dump(), indent=2))
