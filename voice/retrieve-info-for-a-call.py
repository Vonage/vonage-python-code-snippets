import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
VOICE_CALL_ID = os.environ.get('VOICE_CALL_ID')

from vonage import Auth, Vonage
from vonage_voice import CallInfo

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallInfo = client.voice.get_call(VOICE_CALL_ID)
pprint(response)
