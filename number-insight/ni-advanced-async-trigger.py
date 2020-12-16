import nexmo, os
from os.path import join, dirname
from dotenv import load_dotenv
from pprint import pprint

#Load the environment
envpath = join(dirname(__file__),'./.env')
load_dotenv(envpath)

#Init the client
client = nexmo.Client(
    key = os.getenv('NEXMO_API_KEY'),
    secret = os.getenv('NEXMO_API_SECRET')
)

insight_number = input("Enter the number: ")

#Start the trigger
insight_trigger_json = client.get_advanced_number_insight(
    number=insight_number,
    callback=os.getenv('INSIGHT_NUMBER_CALLBACK_WEBHOOK')
)

#If you are in love with the json format you can use the variant below
'''insight_trigger_json = client.get_advanced_number_insight({
    "number": insight_number,
    "callback": os.getenv('INSIGHT_NUMBER_CALLBACK_WEBHOOK')
})
'''

#Get the response from api - the data will be available on callback webhook
pprint(insight_trigger_json)
