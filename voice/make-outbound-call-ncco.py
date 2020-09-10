#!/usr/bin/env python3
import vonage, os
from pprint import pprint

APPLICATION_ID = os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH = os.environ.get("APPLICATION_PRIVATE_KEY_PATH")
VONAGE_NUMBER = os.environ.get("VONAGE_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

client = vonage.Client(
    application_id=APPLICATION_ID, private_key=APPLICATION_PRIVATE_KEY_PATH,
)

voice = vonage.Voice(client)

response = voice.create_call(
    {
        "to": [{"type": "phone", "number": TO_NUMBER}],
        "from": {"type": "phone", "number": VONAGE_NUMBER},
        "ncco": [
            {"action": "talk", "text": "This is a text to speech call from Nexmo"}
        ],
    }
)

pprint(response)
