import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import Archive

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_ARCHIVE_ID = os.getenv("VIDEO_ARCHIVE_ID")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

archive: Archive = vonage_client.video.get_archive(VIDEO_ARCHIVE_ID)

print("=== Got Archive ===")
print(json.dumps(archive.model_dump(), indent=2))
