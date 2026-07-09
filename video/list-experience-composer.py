import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import ListExperienceComposersFilter

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

filter = ListExperienceComposersFilter(offset=0, page_size=5)
ec_list, total, next = vonage_client.video.list_experience_composers(
    filter=filter)

print("=== Total ExperienceComposers ===")
print(total)
print("=== Listed ExperienceComposers ===")
for experience_composer in ec_list:
    print(json.dumps(experience_composer.model_dump(), indent=2))
