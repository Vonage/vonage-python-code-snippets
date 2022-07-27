#!/usr/bin/env python3
import os
from os.path import join, dirname
from pprint import pprint
import vonage
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
UUID = os.environ.get("UUID")

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

dest = {"type": "ncco", "url": ["https://raw.githubusercontent.com/nexmo-community/ncco-examples/gh-pages/text-to-speech.json"]}
response = client.voice.update_call(UUID, action="transfer", destination=dest)
pprint(response)
