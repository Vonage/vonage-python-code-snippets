#!/usr/bin/env python3
import os
from vonage import Voice, Client
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

APPLICATION_ID = os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH = os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

voice = Voice(
    Client(
        application_id=APPLICATION_ID,
        private_key=APPLICATION_PRIVATE_KEY_PATH,
    )
)

# Note call can be made to current call or a completed call
response = voice.get_call("NEXMO_CALL_UUID")
pprint(response)
