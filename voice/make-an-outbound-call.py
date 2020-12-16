#!/usr/bin/env python3
import nexmo
from pprint import pprint

client = nexmo.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

response = client.create_call({
  'to': [{'type': 'phone', 'number': TO_NUMBER}],
  'from': {'type': 'phone', 'number': VONAGE_NUMBER},
  'answer_url': ['https://nexmo-community.github.io/ncco-examples/text-to-speech.json']
})

pprint(response)