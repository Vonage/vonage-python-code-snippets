#!/usr/bin/env python3
import nexmo
from pprint import pprint

client = nexmo.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

response = client.application_v2.list_applications()

pprint(response)
