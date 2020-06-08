# Import dependencies
import nexmo, os
from os.path import join, dirname
from dotenv import load_dotenv

# Load the environment
envpath = join(dirname(__file__), "./.env")
load_dotenv(envpath)

# Init the client
client = nexmo.Client(
    application_id=os.getenv("NEXMO_APPLICATION_ID"),
    private_key=os.getenv("NEXMO_PRIVATE_KEY"),
)

response = client.create_call(
    {
        "to": [{"type": "phone", "number": os.getenv("TO_NUMBER")}],
        "from": {"type": "phone", "number": os.getenv("FROM_NUMBER")},
        "ncco": [
            {
                "action": "talk",
                "text": "This is just a text while we tranfer you to another NCCO",
            }
        ],
    }
)

dest = {
    "type": "ncco",
    "url": [
        "{NGROK_HOST}/{endpoint}".format(
            NGROK_HOST=os.getenv("FROM_NUMBER"), endpoint="webhooks/answer"
        )
    ],
}

response = client.update_call(response["uuid"], action="transfer", destination=dest)


print(response)
