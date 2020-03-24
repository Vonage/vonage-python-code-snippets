#Import the dependencies
import nexmo, os
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint

#Load the environment
envpath = join(dirname(__file__),'./.env')
load_dotenv(envpath)

#Init the client
print(os.getenv("NEXMO_PRIVATE_KEY"))
client = nexmo.Client(
    application_id = os.getenv('NEXMO_APPLICATION_ID'),
    private_key = os.getenv("NEXMO_PRIVATE_KEY")
)

response = client.create_call({
  'to': [{'type': 'phone', 'number': os.getenv('TO_NUMBER')}],
  'from': {'type': 'phone', 'number': os.getenv('FROM_NUMBER')},
  "ncco": [{"action": "talk", "text": "This is an old NCCO that will be replaced with another one"}]
})

# the UUID will appear here, just copy it.. Answer the call and then when speech plays paste the UUID
# And the old NCCO will be replaced with a new one
print(response)

#Enter the UUID of the inbound call here
UUID = input("Enter the UUID: ")

#
response = client.update_call(
    UUID,{
        "action":"transfer",
        "destination":{
            "type": "ncco",
            "ncco": [{"action": "talk", "text": "This is a new NCCO"}]
        }
    }
)

pprint(response)
