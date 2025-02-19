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
        "text": "What do you think of Vonage APIs?",
        "suggestions": [
            {
                "reply": {
                    "text": "They\'re great!",
                    "postbackData": "suggestion_1",
                }
            },
            {
                "reply": {
                    "text": "They\'re awesome!",
                    "postbackData": "suggestion_2",
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
