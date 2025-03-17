import os
from datetime import datetime, timedelta
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
ROOM_DISPLAY_NAME = os.environ.get('ROOM_DISPLAY_NAME')


import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_PRIVATE_KEY,
)

expiration_date = (datetime.utcnow() + timedelta(days=30)).isoformat()

params = {
    'display_name': ROOM_DISPLAY_NAME,
    'type': 'long_term',
    'expires_at': expiration_date,
}

response = client.meetings.create_room(params)
