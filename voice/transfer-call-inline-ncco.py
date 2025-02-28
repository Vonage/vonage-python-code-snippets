import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
UUID = os.environ.get("UUID")

from vonage import Auth, Vonage
from vonage_voice import Talk

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

ncco = [Talk(text='Your call has been transferred to a new NCCO.')]

client.voice.transfer_call_ncco(UUID, ncco)
