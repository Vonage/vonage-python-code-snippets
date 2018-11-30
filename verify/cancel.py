import os
from os.path import join, dirname
import sys
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")

if len(sys.argv) != 2:
    print("Please supply request_id")
    exit()

REQUEST_ID = sys.argv[1]

import nexmo

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

response = client.cancel_verification(REQUEST_ID)

if response["status"] == "0":
    print("Cancellation successful")
else:
    print("Error: %s" % response["error_text"])
