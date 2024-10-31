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

from vonage import Auth, Vonage
from vonage_messages.models import RcsCustom

client = Vonage(
    Auth(
        application_id=VONAGE_APPLICATION_ID,
        private_key=VONAGE_APPLICATION_PRIVATE_KEY_PATH,
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
                                "fileUrl": "'$IMAGE_URL'",
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
                                "fileUrl": "'$VIDEO_URL'",
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
    to=TO_NUMBER,
    from_=RCS_SENDER_ID,
    custom=custom_dict,
)

response = client.messages.send(message)
print(response)
