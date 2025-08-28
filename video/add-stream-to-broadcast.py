import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import AddStreamRequest

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_BROADCAST_ID = os.getenv("VIDEO_BROADCAST_ID")
VIDEO_STREAM_ID = os.getenv("VIDEO_STREAM_ID")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

params = AddStreamRequest(
    stream_id=VIDEO_STREAM_ID,
    has_video=True
)

vonage_client.video.add_stream_to_broadcast(
    broadcast_id=VIDEO_BROADCAST_ID,
    params=params
)

print("=== Added Stream to Broadcast ===")
