# Import dependencies
import os
from os.path import join, dirname
import vonage
from dotenv import load_dotenv
import time

# Load the environment
envpath = join(dirname(__file__), './.env')
load_dotenv(envpath)

# Init the client

client = vonage.Client(
    application_id=os.getenv('VONAGE_APPLICATION_ID'),
    private_key=os.getenv("VONAGE_PRIVATE_KEY")
)

response = client.voice.create_call({
    "to": [{"type": "phone", "number": os.getenv('TO_NUMBER')}],
    "from": {"type": "phone", "number": os.getenv('FROM_NUMBER')},
    "ncco": [
        {
            "action": "talk",
            "text": "This is just a text whilst you tranfer to another NCCO"
        },
        # Play hold music until the call is transferred
        {
            "action": "stream",
            "streamUrl": [
                "https://example.com/hold-music.mp3"
            ],
            "loop": "0"
        }
    ]
})

# Give the recipient time to answer 
time.sleep(5)

response = client.voice.update_call(
    response["uuid"], {
        "action": "transfer",
        "destination": {
            "type": "ncco",
            "ncco": [{"action": "talk", "text": "hello world"}]
        }
    }
)


print(response)
