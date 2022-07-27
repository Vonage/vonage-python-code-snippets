import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get("VONAGE_APPLICATION_PRIVATE_KEY_PATH")

TO_NUMBER = os.environ.get("TO_NUMBER")
FROM_NUMBER = os.environ.get("FROM_NUMBER")

CONTACTS = {
    "type": "contacts",
    "contacts": [
        {
            "addresses": [
                {
                    "city": "Menlo Park",
                    "country": "United States",
                    "country_code": "us",
                    "state": "CA",
                    "street": "1 Hacker Way",
                    "type": "HOME",
                    "zip": "94025",
                },
                {
                    "city": "Menlo Park",
                    "country": "United States",
                    "country_code": "us",
                    "state": "CA",
                    "street": "200 Jefferson Dr",
                    "type": "WORK",
                    "zip": "94025",
                },
            ],
            "birthday": "2012-08-18",
            "emails": [
                {"email": "test@fb.com", "type": "WORK"},
                {"email": "test@whatsapp.com", "type": "WORK"},
            ],
            "name": {
                "first_name": "John",
                "formatted_name": "John Smith",
                "last_name": "Smith",
            },
            "org": {"company": "WhatsApp", "department": "Design", "title": "Manager"},
            "phones": [
                {"phone": "+1 (940) 555-1234", "type": "HOME"},
                {"phone": "+1 (650) 555-1234", "type": "WORK", "wa_id": "16505551234"},
            ],
            "urls": [{"url": "https://www.facebook.com", "type": "WORK"}],
        }
    ],
}

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)


client.messages.send_message(
    {
        "channel": "whatsapp",
        "message_type": "custom",
        "to": TO_NUMBER,
        "from": FROM_NUMBER,
        "custom": CONTACTS,
    }
)
