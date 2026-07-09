import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import Broadcast, CreateBroadcastRequest, ComposedLayout, BroadcastOutputSettings, BroadcastHls, BroadcastRtmp, VideoResolution, LayoutType, StreamMode

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

options = CreateBroadcastRequest(
    session_id=VIDEO_SESSION_ID,
    layout=ComposedLayout(
        type=LayoutType.BEST_FIT,
        screenshare_type=LayoutType.HORIZONTAL_PRESENTATION
    ),
    outputs=BroadcastOutputSettings(
        hls=BroadcastHls(dvr=False, low_latency=True),
        rtmp=[
            BroadcastRtmp(
                id='TEST',
                server_url='rtmp://a.rtmp.youtube.com/live2',
                stream_name='abc123...',
            )
        ],
    ),
    resolution=VideoResolution.RES_1280x720,
    stream_mode=StreamMode.AUTO,
    max_duration=3600,
    max_bitrate=1_000_000,
)
broadcast: Broadcast = vonage_client.video.start_broadcast(options)

print("=== Started Broadcast ===")
print(json.dumps(broadcast.model_dump(), indent=2))
