import os
from os.path import join, dirname
import vonage
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")
VONAGE_REDACT_ID = os.environ.get("VONAGE_REDACT_ID")
VONAGE_REDACT_TYPE = os.environ.get("VONAGE_REDACT_TYPE")
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

# NOTE: THIS IS DEPRECATED AND WILL BE REMOVED IN A LATER RELEASE
redact = vonage.Redact(client)
redact.redact_transaction(id=VONAGE_REDACT_ID, product=VONAGE_REDACT_TYPE)

print("Successfully redacted ID " + VONAGE_REDACT_ID)