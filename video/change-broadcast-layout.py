import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import Broadcast, ComposedLayout, LayoutType

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_BROADCAST_ID = os.getenv("VIDEO_BROADCAST_ID")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

broadcast: Broadcast = vonage_client.video.change_broadcast_layout(
    broadcast_id=VIDEO_BROADCAST_ID,
    layout=ComposedLayout(type=LayoutType.VERTICAL_PRESENTATION),
)

print("=== Changed Broadcast Layout ===")
print(json.dumps(broadcast.model_dump(), indent=2))
