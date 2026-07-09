import os
from dotenv import load_dotenv
import json

from vonage import Auth, Vonage
from vonage_video.models import ListArchivesFilter

load_dotenv()

VONAGE_APPLICATION_ID = os.getenv("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.getenv("VONAGE_PRIVATE_KEY")

vonage_client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

filter = ListArchivesFilter(offset=0, page_size=5)
archive_list, total, next = vonage_client.video.list_archives(filter=filter)

print("=== Total Archives ===")
print(total)
print("=== Listed Archives ===")
for archive in archive_list:
    print(json.dumps(archive.model_dump(), indent=2))
