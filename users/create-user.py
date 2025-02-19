import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_APPLICATION_ID = os.getenv('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.getenv('VONAGE_PRIVATE_KEY')
USER_NAME = os.getenv('USER_NAME')
USER_DISPLAY_NAME = os.getenv('USER_DISPLAY_NAME')

from vonage import Auth, Vonage
from vonage_users import Channels, PstnChannel, User

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

user_options = User(
    name=USER_NAME,
    display_name=USER_DISPLAY_NAME,
    channels=Channels(pstn=[PstnChannel(number=123456)]),
)
user = client.users.create_user(user_options)

print(user)
