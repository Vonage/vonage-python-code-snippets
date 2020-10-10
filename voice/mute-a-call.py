#!/usr/bin/env python3
import time
import os
from os.path import join, dirname
from pprint import pprint
from vonage import Voice
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
UUID = os.environ.get("UUID")

voice = Voice(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH
)

response = voice.update_call(UUID, action="mute")
pprint(response)
time.sleep(5)
response = voice.update_call(UUID, action="unmute")
pprint(response)
