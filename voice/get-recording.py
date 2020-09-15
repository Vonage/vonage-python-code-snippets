#!/usr/bin/env python3
import vonage os
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

APPLICATION_ID=os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH=os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

client = vonage.Client(
    application_id=APPLICATION_ID,
    private_key=APPLICATION_PRIVATE_KEY_PATH,
)

response = client.get_recording(URL)
pprint(response)

