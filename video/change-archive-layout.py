import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import Archive, ComposedLayout, LayoutType

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

archive: Archive = vonage_client.video.change_archive_layout(
    archive_id=VIDEO_ARCHIVE_ID,
    layout=ComposedLayout(type=LayoutType.VERTICAL_PRESENTATION),
)

print("=== Changed Archive Layout ===")
print(json.dumps(archive.model_dump(), indent=2))
