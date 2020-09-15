import argparse
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("request_id")
argument_parser.add_argument("verification_code")
arguments = argument_parser.parse_args()

REQUEST_ID = arguments.request_id
CODE = arguments.verification_code

import vonage

verify = vonage.Verify(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

response = verify.check(REQUEST_ID, code=CODE)

if response["status"] == "0":
    print("Verification successful, event_id is %s" % (response["event_id"]))
else:
    print("Error: %s" % response["error_text"])
