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
from vonage_messages.models import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_PRIVATE_KEY,
    )
)

custom_dict = {
    "contentMessage": {
        "text": "Product Launch: Save the date!",
        "suggestions": [
            {
                "action": {
                    "text": "Save to calendar",
                    "postbackData": "postback_data_1234",
                    "fallbackUrl": "https://www.google.com/calendar",
                    "createCalendarEventAction": {
                        "startTime": "2024-06-28T19:00:00Z",
                        "endTime": "2024-06-28T20:00:00Z",
                        "title": "Vonage API Product Launch",
                        "description": "Event to demo Vonage\'s new and exciting API product",
                    },
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
