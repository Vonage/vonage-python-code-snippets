import vonage, os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID=os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH=os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
VONAGE_CALL_UUID = os.environ.get("UUID")

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

voice = vonage.Voice(client)

voice.send_dtmf(VONAGE_CALL_UUID, digits='1234')
