import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
TO_NUMBER = os.environ.get("TO_NUMBER")
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")

from vonage import Auth, Vonage
from vonage_messages.models import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Need some help? Call us now or visit our website for more information.",
        "suggestions": [
            {
                "action": {
                    "text": "Call us",
                    "postbackData": "postback_data_1234",
                    "fallbackUrl": "https://www.example.com/contact/",
                    "dialAction": {"phoneNumber": "+447900000000"},
                }
            },
            {
                "action": {
                    "text": "Visit site",
                    "postbackData": "postback_data_1234",
                    "openUrlAction": {"url": "http://example.com/"},
                }
            },
        ],
    }
}

message = RcsCustom(
    to=TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
