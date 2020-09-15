#!/usr/bin/env python3
from vonage import Voice
import time, os
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID=os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH=os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

voice = Voice(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

response = voice.update_call(UUID, action="earmuff")
pprint(response)
time.sleep(5)
response = voice.update_call(UUID, action="unearmuff")
pprint(response)
