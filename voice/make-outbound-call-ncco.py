#!/usr/bin/env python3
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')

VONAGE_NUMBER = os.environ.get('VONAGE_NUMBER')
TO_NUMBER = os.environ.get('TO_NUMBER')

from vonage import Auth, Vonage
from vonage_voice import CreateCallRequest, Phone, Talk, ToPhone

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response = client.voice.create_call(
    CreateCallRequest(
        ncco=[Talk(text='Hello world')],
        to=[ToPhone(number=TO_NUMBER)],
        from_=Phone(number=VONAGE_NUMBER),
    )
)

pprint(response)
