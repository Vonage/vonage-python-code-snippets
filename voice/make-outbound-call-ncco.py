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
    'ncco': [
        {
            'action': 'talk',
            'text': 'You are listening to a test text-to-speech call made with the Vonage Voice API',
            "language": "en-AU",
            "style": 3
        }
    ]
})

pprint(response)
