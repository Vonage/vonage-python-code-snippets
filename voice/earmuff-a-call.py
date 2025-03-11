import os
from os.path import join, dirname
from time import sleep
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
VOICE_CALL_ID = os.environ.get('VOICE_CALL_ID')


from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

client.voice.earmuff(VOICE_CALL_ID)
sleep(3)
client.voice.unearmuff(VOICE_CALL_ID)
