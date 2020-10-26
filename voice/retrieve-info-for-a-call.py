#!/usr/bin/env python3
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv
from vonage import Voice, Client

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")
VONAGE_CALL_UUID = os.environ.get("UUID")

voice = Voice(
    Client(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

# Note call can be made to current call or a completed call
response = voice.get_call(VONAGE_CALL_UUID)
pprint(response)
