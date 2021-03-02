import os
from os.path import join, dirname
import vonage
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")
VONAGE_SECRET_ID = os.environ.get("VONAGE_SECRET_ID")
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

secret = client.get_secret(api_key=VONAGE_API_KEY, secret_id=VONAGE_SECRET_ID)
print(secret["id"] + ": Created on " + secret["created_at"])