import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
TO_NUMBER = os.environ.get("TO_NUMBER")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER")
CATALOG_ID = os.environ.get('CATALOG_ID')
PRODUCT_RETAILER_ID = os.environ.get('PRODUCT_RETAILER_ID')

from vonage import Auth, Vonage
from vonage_messages.models import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=TO_NUMBER,
    from_=WHATSAPP_NUMBER,
    custom={
        'type': 'interactive',
        'interactive': {
            'type': 'product',
            'body': {'text' 'Check out this cool product'},
            'footer': {'text': 'Sale now on!'},
            'action': {
                'catalog_id': CATALOG_ID,
                'product_retailer_id': PRODUCT_RETAILER_ID,
            },
        },
    },
)

response = client.messages.send(message)
print(response)
