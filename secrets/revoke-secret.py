import os
from os.path import join, dirname
from dotenv import load_dotenv
import vonage

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

# Init the client
client = vonage.Client(
    key=os.getenv("VONAGE_API_KEY"), secret=os.getenv("VONAGE_API_SECRET")
)

try:
    # Get the data from standard input
    api_key = os.getenv("VONAGE_API_KEY")
    secret_id = os.getenv("VONAGE_SECRET_ID")
    client.account.delete_secret(api_key, secret_id)
    print("Secret removed")
except:
    print("Error when try to removing secret")
