# Import dependencies
import os
from os.path import join, dirname
import vonage
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), './.env')
load_dotenv(envpath)

# Init the client

client = vonage.Client(
    application_id=os.getenv('VONAGE_APPLICATION_ID'),
    private_key=os.getenv("VONAGE_PRIVATE_KEY")
)

voice = vonage.Voice(client)

response = voice.create_call({
    "to": [{"type": "phone", "number": os.getenv('TO_NUMBER')}],
    "from": {"type": "phone", "number": os.getenv('FROM_NUMBER')},
    "ncco": [
        {
            "action": "talk",
            "text": "This is just a text whilst you tranfer to another NCCO"
        }
    ]
})

response = voice.update_call(
    response["uuid"], {
        "action": "transfer",
        "destination": {
            "type": "ncco",
            "ncco": [{"action": "talk", "text": "hello world"}]
        }
    }
)


print(response)
