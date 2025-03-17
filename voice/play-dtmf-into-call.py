import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
VOICE_CALL_ID = os.environ.get('VOICE_CALL_ID')
VOICE_DTMF_DIGITS = os.environ.get('VOICE_DTMF_DIGITS')

from vonage import Auth, Vonage
from vonage_voice import CallMessage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_dtmf_into_call(
    uuid=VOICE_CALL_ID, dtmf=VOICE_DTMF_DIGITS
)

pprint(response)
