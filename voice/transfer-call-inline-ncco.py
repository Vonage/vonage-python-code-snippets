# Import dependencies
import nexmo
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), './.env')
load_dotenv(envpath)

# Init the client
print(os.getenv("NEXMO_PRIVATE_KEY"))
client = nexmo.Client(
    application_id=os.getenv('NEXMO_APPLICATION_ID'),
    private_key=os.getenv("NEXMO_PRIVATE_KEY")
)

response = client.create_call({
    "to": [{"type": "phone", "number": os.getenv('TO_NUMBER')}],
    "from": {"type": "phone", "number": os.getenv('FROM_NUMBER')},
    "ncco": [
        {
            "action": "talk",
            "text": "This is just a text whilst you tranfer to another NCCO"
        }
    ]
})

response = client.update_call(
    response["uuid"], {
        "action": "transfer",
        "destination": {
            "type": "ncco",
            "ncco": [{"action": "talk", "text": "hello world"}]
        }
    }
)


print(response)
