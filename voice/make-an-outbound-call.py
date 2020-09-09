#!/usr/bin/env python3
import vonage, os
from pprint import pprint

APPLICATION_ID=os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH=os.environ.get("APPLICATION_PRIVATE_KEY_PATH")
NEXMO_NUMBER=os.environ.get("NEXMO_NUMBER")
TO_NUMBER=os.environ.get("TO_NUMBER")

client = vonage.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

voice = vonage.Voice(client)

response = voice.create_call({
  'to': [{'type': 'phone', 'number': TO_NUMBER}],
  'from': {'type': 'phone', 'number': NEXMO_NUMBER},
  'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
})

pprint(response)