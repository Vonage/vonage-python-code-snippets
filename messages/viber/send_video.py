import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

TO_NUMBER = os.environ.get("TO_NUMBER")
VIBER_SERVICE_MESSAGE_ID = os.environ.get("VIBER_SERVICE_MESSAGE_ID")

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.messages.send_message(
    {
        'channel': 'viber_service',
        'message_type': 'video',
        'to': TO_NUMBER,
        'from': VIBER_SERVICE_MESSAGE_ID,
        'video': {
            'url': 'https://example.com/video.mp4',
            'caption': 'Look at this video',
            'thumb_url': 'https://example.com/thumbnail.jpg',
        },
        'viber_service': {'category': 'transaction', 'duration': '120', 'ttl': 30, 'type': 'string'},
    }
)
