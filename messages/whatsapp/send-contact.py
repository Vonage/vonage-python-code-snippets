import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
WHATSAPP_SENDER_ID = os.environ.get("WHATSAPP_SENDER_ID")

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
                "org": {
                    "company": "WhatsApp",
                    "department": "Design",
                    "title": "Manager",
                },
                "phones": [
                    {"phone": "+1 (940) 555-1234", "type": "HOME"},
                    {
                        "phone": "+1 (650) 555-1234",
                        "type": "WORK",
                        "wa_id": "16505551234",
                    },
                ],
                "urls": [{"url": "https://www.facebook.com", "type": "WORK"}],
            }
        ],
    },
)

response = client.messages.send(message)
print(response)
