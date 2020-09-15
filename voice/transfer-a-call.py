#!/usr/bin/env python3
import vonage, os
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID=os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH=os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

voice = vonage.Voice(client)

dest = {"type": "ncco", "url": ["https://developer.nexmo.com/ncco/tts.json"]}
response = voice.update_call(UUID, action="transfer", destination=dest)
pprint(response)
