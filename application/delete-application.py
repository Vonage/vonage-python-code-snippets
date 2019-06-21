#!/usr/bin/env python3
import nexmo
from pprint import pprint

client = nexmo.Client(
    key=NEXMO_API_KEY,
    secret=NEXMO_API_SECRET
)

response = client.application_v2.delete_application(NEXMO_APPLICATION_ID)

pprint(response)
