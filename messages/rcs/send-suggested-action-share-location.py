import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")

from vonage import Auth, Vonage
from vonage_messages import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Your driver will come and meet you at your specified location.",
        "suggestions": [
            {
                "action": {
                    "text": "Share a location",
                    "postbackData": "postback_data_1234",
                    "shareLocationAction": {},
                }
            }
        ],
    }
}


message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
