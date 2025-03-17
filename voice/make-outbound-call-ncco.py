from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
VOICE_TO_NUMBER = os.environ.get('VOICE_TO_NUMBER')
VONAGE_VIRTUAL_NUMBER = os.environ.get('VONAGE_VIRTUAL_NUMBER')

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
        ncco=[Talk(text='This is a text to speech call from Vonage.')],
        to=[ToPhone(number=VOICE_TO_NUMBER)],
        from_=Phone(number=VONAGE_VIRTUAL_NUMBER),
    )
)

pprint(response)
