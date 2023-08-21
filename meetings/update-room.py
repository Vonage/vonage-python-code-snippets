import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get('VONAGE_APPLICATION_PRIVATE_KEY_PATH')
ROOM_ID = os.environ.get('ROOM_ID')
THEME_ID = os.environ.get('THEME_ID')

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

params = {'update_details': {'theme_id': THEME_ID}}
response = client.meetings.update_room(ROOM_ID, params)
