#!/usr/bin/env python3
import vonage, os
from pprint import pprint
from datetime import datetime, timedelta
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

APPLICATION_ID = os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH = os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

voice = vonage.Voice(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

NOW = datetime.utcnow()
DATE_END = NOW.replace(microsecond=0).isoformat()+"Z"
DATE_START = (NOW - timedelta(hours=24, minutes=00)).replace(microsecond=0).isoformat()+"Z"

response = voice.get_calls(date_start=DATE_START, date_end=DATE_END)
calls = response['_embedded']['calls']
for call in calls:
    pprint(call)
