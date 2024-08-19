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
                "richCard": {
                    "standaloneCard": {
                        "thumbnailImageAlignment": "RIGHT",
                        "cardOrientation": "VERTICAL",
                        "cardContent": {
                            "title": "Quick question",
                            "description": "Do you like this picture?",
                            "media": {
                                "height": "TALL",
                                "contentInfo": {
                                    "fileUrl": "'$IMAGE_URL'",
                                    "forceRefresh": "false",
                                },
                            },
                            "suggestions": [
                                {
                                    "reply": {
                                        "text": "Yes",
                                        "postbackData": "suggestion_1",
                                    }
                                },
                                {
                                    "reply": {
                                        "text": "I love it!",
                                        "postbackData": "suggestion_2",
                                    }
                                },
                            ],
                        },
                    }
                }
            }
        },
    }
)
