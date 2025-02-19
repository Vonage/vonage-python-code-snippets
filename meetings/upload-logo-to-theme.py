import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get('VONAGE_APPLICATION_ID')
VONAGE_PRIVATE_KEY = os.environ.get('VONAGE_PRIVATE_KEY')
THEME_ID = os.environ.get('THEME_ID')

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_PRIVATE_KEY,
)

response = client.meetings.upload_logo_to_theme(
    theme_id=THEME_ID,
    path_to_image='path/to/my_image.png',
    logo_type='favicon',
)
