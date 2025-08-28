import os
from dotenv import load_dotenv
import time

from vonage import Auth, Vonage
from vonage_video.models import TokenOptions

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

token = vonage_client.video.generate_client_token(
    TokenOptions(
        session_id=VIDEO_SESSION_ID,
        role="moderator",
        connection_data="",
        expire_time=int(time.time()) + 600,  # 600sec=10min
    )
)

if isinstance(token, bytes):
    token = token.decode("utf-8")

print("=== Generated token ===")
print(token)
