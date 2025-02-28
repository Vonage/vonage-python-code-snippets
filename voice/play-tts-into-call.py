import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')

CALL_UUID = os.environ.get('CALL_UUID')
LANGUAGE = os.environ.get('LANGUAGE')

from vonage import Auth, Vonage
from vonage_voice import CallMessage, TtsStreamOptions


client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_tts_into_call(
    uuid=CALL_UUID,
    tts_options=TtsStreamOptions(text='Hello from Vonage.', language=LANGUAGE),
)

pprint(response)
