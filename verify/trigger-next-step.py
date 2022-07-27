import argparse
import os
from os.path import join, dirname
from dotenv import load_dotenv
import vonage

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("request_id")
arguments = argument_parser.parse_args()

REQUEST_ID = arguments.request_id

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

response = client.verify.trigger_next_event(REQUEST_ID)

if response["status"] == "0":
    print("Next verification stage triggered")
else:
    print("Error: %s" % response["error_text"])
