import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

VONAGE_APPLICATION_ID = os.environ.get("VONAGE_APPLICATION_ID")
VONAGE_PRIVATE_KEY = os.environ.get("VONAGE_PRIVATE_KEY")
MESSAGES_TO_NUMBER = os.environ.get("MESSAGES_TO_NUMBER")
RCS_SENDER_ID = os.environ.get("RCS_SENDER_ID")
MESSAGES_IMAGE_URL = os.environ.get("MESSAGES_IMAGE_URL")
MESSAGES_VIDEO_URL = os.environ.get("MESSAGES_VIDEO_URL")

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
        "richCard": {
            "carouselCard": {
                "cardWidth": "MEDIUM",
                "cardContents": [
                    {
                        "title": "Option 1: Photo",
                        "description": "Do you prefer this photo?",
                        "suggestions": [
                            {
                                "reply": {
                                    "text": "Option 1",
                                    "postbackData": "card_1",
                                }
                            }
                        ],
                        "media": {
                            "height": "MEDIUM",
                            "contentInfo": {
                                "fileUrl": MESSAGES_IMAGE_URL,
                                "forceRefresh": "false",
                            },
                        },
                    },
                    {
                        "title": "Option 2: Video",
                        "description": "Or this video?",
                        "suggestions": [
                            {
                                "reply": {
                                    "text": "Option 2",
                                    "postbackData": "card_2",
                                }
                            }
                        ],
                        "media": {
                            "height": "MEDIUM",
                            "contentInfo": {
                                "fileUrl": MESSAGES_VIDEO_URL,
                                "forceRefresh": "false",
                            },
                        },
                    },
                ],
            }
        }
    }
}

message = RcsCustom(
    to=MESSAGES_TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
