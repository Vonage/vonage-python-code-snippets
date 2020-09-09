import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
NUMBER_SEARCH_CRITERIA = os.getenv("NUMBER_SEARCH_CRITERIA")
NUMBER_SEARCH_PATTERN = os.getenv("NUMBER_SEARCH_PATTERN")
NEXMO_NUMBER_TYPE = os.getenv("NEXMO_NUMBER_TYPE")
NEXMO_NUMBER_FEATURES = os.getenv("NEXMO_NUMBER_FEATURES")

import vonage

client = vonage.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

responseData = client.get_available_numbers(
    COUNTRY_CODE,
    {
        "pattern": NUMBER_SEARCH_CRITERIA,
        "search_pattern": NUMBER_SEARCH_PATTERN,
        "type": NEXMO_NUMBER_TYPE,
        "features": NEXMO_NUMBER_FEATURES,
    },
)

print(
    f'Here are {len(responseData["numbers"])} of the {responseData["count"]} matching numbers available for purchase:'
)

for number in responseData["numbers"]:
    print(f'Tel: {number["msisdn"]} Cost: {number["cost"]}')
