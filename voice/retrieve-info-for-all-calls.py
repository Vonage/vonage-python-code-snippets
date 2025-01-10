from datetime import datetime, timedelta, timezone
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    'VONAGE_APPLICATION_PRIVATE_KEY_PATH'
)

from vonage import Auth, Vonage
from vonage_voice.models import ListCallsFilter

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)


NOW = datetime.now(timezone.utc)
DATE_END = NOW.replace(microsecond=0).isoformat()
DATE_START = (NOW - timedelta(hours=24, minutes=00)).replace(microsecond=0).isoformat()

calls, _ = client.voice.list_calls(
    ListCallsFilter(date_start=DATE_START, date_end=DATE_END)
)

for call in calls:
    pprint(call)
