#!/usr/bin/env python3
import nexmo
from pprint import pprint

client = nexmo.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

dest = {"type": "ncco", "url": ["https://nexmo-community.github.io/ncco-examples/transfer.json"]}
response = client.update_call(UUID, action="transfer", destination=dest)
pprint(response)
