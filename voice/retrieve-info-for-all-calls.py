#!/usr/bin/env python3
import nexmo
from pprint import pprint
from datetime import datetime, timedelta

client = nexmo.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

DATE_END = datetime.utcnow().replace(microsecond=0).isoformat()+"Z"
DATE_START = (datetime.utcnow() - timedelta(hours=24, minutes=00)).replace(microsecond=0).isoformat()+"Z"

params = {"date_start": DATE_START, "date_end": DATE_END}
response = client.get_calls(params)
calls = response['_embedded']['calls']
for call in calls:
    pprint(call)
