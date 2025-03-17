from datetime import datetime, timedelta, timezone
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')

from vonage import Auth, Vonage
from vonage_voice import ListCallsFilter

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

now = datetime.now(timezone.utc)
date_end = now.strftime('%Y-%m-%dT%H:%M:%SZ')
start = now - timedelta(hours=24)
date_start = start.strftime('%Y-%m-%dT%H:%M:%SZ')

calls, _ = client.voice.list_calls(
    ListCallsFilter(date_start=date_start, date_end=date_end)
)

for call in calls:
    pprint(call)
