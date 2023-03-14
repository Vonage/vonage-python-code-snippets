import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

TO_NUMBER = os.environ.get("TO_NUMBER")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER")

CATALOG_ID = os.environ.get('CATALOG_ID')
PRODUCT_RETAILER_ID = os.environ.get('PRODUCT_RETAILER_ID')

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.messages.send_message(
    {
        'to': TO_NUMBER,
        'from': WHATSAPP_NUMBER,
        'channel': 'whatsapp',
        'message_type': 'custom',
        'custom': {
            'type': 'interactive',
            'interactive': {
                'type': 'product',
                'body': {'text' 'Check out this cool product'},
                'footer': {'text': 'Sale now on!'},
                'action': {'catalog_id': CATALOG_ID, 'product_retailer_id': PRODUCT_RETAILER_ID},
            },
        },
    }
)
