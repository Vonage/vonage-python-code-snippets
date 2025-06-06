import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
VOICE_CALL_ID = os.environ.get("VOICE_CALL_ID")

from vonage import Auth, Vonage
from vonage_voice import Talk

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

ncco = [Talk(text='This is a transfer action using an inline NCCO')]

client.voice.transfer_call_ncco(VOICE_CALL_ID, ncco)
