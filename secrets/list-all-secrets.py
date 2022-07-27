import os
from os.path import join, dirname
import vonage
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
API_KEY = os.environ.get("VONAGE_API_KEY")
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

secrets = client.account.list_secrets(api_key=API_KEY)
for secret in secrets["_embedded"]["secrets"]:
    print(secret["id"] + ": Created on " + secret["created_at"])