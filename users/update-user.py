import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "../.env")
load_dotenv(envpath)

VONAGE_APPLICATION_ID = os.getenv('VONAGE_APPLICATION_ID')
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.getenv('VONAGE_APPLICATION_PRIVATE_KEY_PATH')
USER_NEW_NAME = os.getenv('USER_NEW_NAME')
USER_NEW_DISPLAY_NAME = os.getenv('USER_NEW_DISPLAY_NAME')
USER_ID = os.getenv('USER_ID')

from vonage import Auth, Vonage
from vonage_users import Channels, PstnChannel, SmsChannel, User

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
    )
)

user_params = User(
    name=USER_NEW_NAME,
    display_name=USER_NEW_DISPLAY_NAME,
    channels=Channels(
        sms=[SmsChannel(number='1234567890')], pstn=[PstnChannel(number=123456)]
    ),
)
user: User = client.users.update_user(id=USER_ID, params=user_params)

print(user)
