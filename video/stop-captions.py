import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import CaptionsData

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_CAPTIONS_ID = os.getenv("VIDEO_CAPTIONS_ID")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

vonage_client.video.stop_captions(
    CaptionsData(captions_id=VIDEO_CAPTIONS_ID)
)

print("=== Stopped Captions ===")
