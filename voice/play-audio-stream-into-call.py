import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')

CALL_UUID = os.environ.get('CALL_UUID')

from vonage import Auth, Vonage
from vonage_voice import AudioStreamOptions, CallMessage


client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

response: CallMessage = client.voice.play_audio_into_call(
    CALL_UUID,
    audio_stream_options=AudioStreamOptions(
        stream_url=['https://example.com/ringtone.mp3']
    ),
)

pprint(response)
