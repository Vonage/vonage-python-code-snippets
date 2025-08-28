import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import ExperienceComposer, ExperienceComposerOptions, ExperienceComposerProperties, VideoResolution

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")
VIDEO_SESSION_ID = os.getenv("VIDEO_SESSION_ID")
VIDEO_TOKEN = os.getenv("VIDEO_TOKEN")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

options = ExperienceComposerOptions(
    session_id=VIDEO_SESSION_ID,
    token=VIDEO_TOKEN,
    url='https://developer.vonage.com',
    max_duration=3600,
    resolution=VideoResolution.RES_1280x720,
    properties=ExperienceComposerProperties(name='TEST'),
)
experience_composer: ExperienceComposer = vonage_client.video.start_experience_composer(
    options)

print("=== Started ExperienceComposer ===")
print(json.dumps(experience_composer.model_dump(), indent=2))
