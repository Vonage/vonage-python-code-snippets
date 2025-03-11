#!/usr/bin/env python3
import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
FROM_NUMBER = os.environ.get("FROM_NUMBER")
VOICE_TO_NUMBER = os.environ.get("VOICE_TO_NUMBER")

from vonage import Auth, Vonage
from vonage_voice import CreateCallRequest, Phone, ToPhone

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.voice.create_call(
    CreateCallRequest(
        answer_url=[
            'https://raw.githubusercontent.com/nexmo-community/ncco-examples/gh-pages/text-to-speech.json'
        ],
        to=[ToPhone(number=VOICE_TO_NUMBER)],
        from_=Phone(number=FROM_NUMBER),
    )
)

pprint(response)
