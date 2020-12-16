# Import dependencies
import nexmo
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), './.env')
load_dotenv(envpath)

# Init the nexmo client
client = nexmo.Client(
    application_id=os.getenv('NEXMO_APPLICATION_ID'),
    private_key=os.getenv("NEXMO_PRIVATE_KEY")
)

UUID = os.getenv('CALL_UUID')

#Update the current NCCO with a new one 
response = client.update_call(
    UUID, {
        "action": "transfer",
        "destination": {
            "type": "ncco",
            "ncco": [{"action": "talk", "text": "Hello, thank you for using the Vonage API. If you can hear this message, then transfer to a new NCCO worked."}]
        }
    }
)


print(response)
