import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_APPLICATION_ID = os.getenv('VONAGE_APPLICATION_ID')
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.getenv('VONAGE_APPLICATION_PRIVATE_KEY_PATH')
USER_ID = os.getenv('USER_ID')

from vonage import Auth, Vonage

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)
client.users.delete_user(USER_ID)
