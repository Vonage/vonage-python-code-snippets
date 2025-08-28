import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import SessionOptions

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

options = SessionOptions(
    location="125.125.224.224",
    e2ee="false",
    media_mode="routed",
    archive_mode="manual",
    archiveName="TEST",
    archiveResolution="1920x1080"
)
session = vonage_client.video.create_session(options)

print("=== Created Session ===")
print(json.dumps(session.model_dump(), indent=2))
