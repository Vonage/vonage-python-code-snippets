
import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv
import vonage

#Load the environment
envpath = join(dirname(__file__), '../.env')
load_dotenv(envpath)

#Init the client
client = vonage.Client(
    key=os.getenv('VONAGE_API_KEY'),
    secret=os.getenv('VONAGE_API_SECRET')
)

insight_number = os.getenv('INSIGHT_NUMBER')

#Start the trigger
insight_trigger_json = client.get_async_advanced_number_insight(
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
