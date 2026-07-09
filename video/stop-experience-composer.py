import os
from dotenv import load_dotenv

from vonage import Auth, Vonage

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_EC_ID = os.getenv("VIDEO_EC_ID")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

vonage_client.video.stop_experience_composer(VIDEO_EC_ID)

print("=== Stopped ExperienceComposer ===")
