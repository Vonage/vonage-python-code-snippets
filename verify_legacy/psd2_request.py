import os
from os.path import join, dirname
from dotenv import load_dotenv
import vonage

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")
RECIPIENT_NUMBER = os.environ.get("RECIPIENT_NUMBER")
PAYEE = os.environ.get("PAYEE")
AMOUNT = os.environ.get("AMOUNT")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

response = client.verify.psd2(number=RECIPIENT_NUMBER, payee=PAYEE, amount=AMOUNT)

if response["status"] == "0":
    print("Started PSD2 verification request_id is %s" % (response["request_id"]))
else:
    print("Error: %s" % response["error_text"])
