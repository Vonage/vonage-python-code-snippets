import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import ExperienceComposer

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

experience_composer: ExperienceComposer = vonage_client.video.get_experience_composer(
    VIDEO_EC_ID)

print("=== Got ExperienceComposer ===")
print(json.dumps(experience_composer.model_dump(), indent=2))
