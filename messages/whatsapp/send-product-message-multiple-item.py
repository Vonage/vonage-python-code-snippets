import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")
WHATSAPP_CATALOG_ID = os.environ.get('WHATSAPP_CATALOG_ID')
WHATSAPP_PRODUCT_ID_1 = os.environ.get('WHATSAPP_PRODUCT_ID_1')
WHATSAPP_PRODUCT_ID_2 = os.environ.get('WHATSAPP_PRODUCT_ID_2')

from vonage import Auth, Vonage
from vonage_messages import WhatsappCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

message = WhatsappCustom(
    to=MESSAGES_TO_NUMBER,
    from_=WHATSAPP_SENDER_ID,
    custom={
        'type': 'interactive',
        'interactive': {
            'type': 'product_list',
            'header': {'type': 'text', 'text': 'Our top products'},
            'body': {'text': 'Check out these great products'},
            'footer': {'text': 'Sale now on!'},
            'action': {
                'catalog_id': WHATSAPP_CATALOG_ID,
                'sections': [
                    {
                        'title': 'Cool products',
                        'product_items': [
                            {'WHATSAPP_PRODUCT_ID_1': WHATSAPP_PRODUCT_ID_1},
                            {'WHATSAPP_PRODUCT_ID_2': WHATSAPP_PRODUCT_ID_2},
                        ],
                    },
                    {
                        'title': 'Awesome products',
                        'product_items': [
                            {'WHATSAPP_PRODUCT_ID_1': WHATSAPP_PRODUCT_ID_1}
                        ],
                    },
                ],
            },
        },
    },
)

response = client.messages.send(message)
print(response)
