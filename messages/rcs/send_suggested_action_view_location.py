import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_APPLICATION_PRIVATE_KEY_PATH = os.environ.get(
    "VONAGE_APPLICATION_PRIVATE_KEY_PATH"
)

TO_NUMBER = os.environ.get("TO_NUMBER")
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")

import vonage

client = vonage.Client(
    application_id=VONAGE_APPLICATION_ID,
    private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
)

client.messages.send_message(
    {
        "channel": "rcs",
        "message_type": "custom",
        "to": TO_NUMBER,
        "from": RCS_SENDER_ID,
        "custom": {
            "contentMessage": {
                "text": "Drop by our office!",
                "suggestions": [
                    {
                        "action": {
                            "text": "View map",
                            "postbackData": "postback_data_1234",
                            "fallbackUrl": "https://www.google.com/maps/place/Vonage/@51.5230371,-0.0852492,15z",
                            "viewLocationAction": {
                                "latLong": {
                                    "latitude": "51.5230371",
                                    "longitude": "-0.0852492",
                                },
                                "label": "Vonage London Office",
                            },
                        }
                    }
                ],
            }
        },
    }
)
