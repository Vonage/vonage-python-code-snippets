import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import Archive, CreateArchiveRequest

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_SESSION_ID = os.getenv("VIDEO_SESSION_ID")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

options = CreateArchiveRequest(
    session_id=VIDEO_SESSION_ID,
    stream_mode="auto",
    output_mode="composed",
    resolution='1280x720',
    has_audio=True,
    has_video=True,
)
archive: Archive = vonage_client.video.start_archive(options)

print("=== Started Archive ===")
print(json.dumps(archive.model_dump(), indent=2))
