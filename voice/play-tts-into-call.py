import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
VOICE_CALL_ID = os.environ.get('VOICE_CALL_ID')
VOICE_TEXT = os.environ.get('VOICE_TEXT')
VOICE_LANGUAGE = os.environ.get('VOICE_LANGUAGE')

from vonage import Auth, Vonage
from vonage_voice import CallMessage, TtsStreamOptions


client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_tts_into_call(
    uuid=VOICE_CALL_ID,
    tts_options=TtsStreamOptions(text=VOICE_TEXT, language=VOICE_LANGUAGE),
)

pprint(response)
