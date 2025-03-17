import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
THEME_ID = os.environ.get('THEME_ID')
MAIN_COLOR = os.environ.get('MAIN_COLOR')
BRAND_TEXT = os.environ.get('BRAND_TEXT')

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_PRIVATE_KEY,
)

response = client.meetings.update_theme(
    THEME_ID,
    {
        'main_color': MAIN_COLOR,
        'brand_text': BRAND_TEXT,
    },
)
