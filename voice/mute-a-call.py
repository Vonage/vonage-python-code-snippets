import os
from os.path import join, dirname
from time import sleep
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    'VONAGE_APPLICATION_PRIVATE_KEY_PATH'
)

CALL_UUID = os.environ.get('CALL_UUID')

from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

client.voice.mute(CALL_UUID)
sleep(5)
client.voice.unmute(CALL_UUID)
