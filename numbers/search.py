import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
NUMBER_SEARCH_CRITERIA = os.getenv("NUMBER_SEARCH_CRITERIA")
NUMBER_SEARCH_PATTERN = os.getenv("NUMBER_SEARCH_PATTERN")
VONAGE_NUMBER_TYPE = os.getenv("VONAGE_NUMBER_TYPE")
VONAGE_NUMBER_FEATURES = os.getenv("VONAGE_NUMBER_FEATURES")

import vonage

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

responseData = client.numbers.get_available_numbers(
    COUNTRY_CODE,
    {
        "pattern": NUMBER_SEARCH_CRITERIA,
        "search_pattern": NUMBER_SEARCH_PATTERN,
        "type": VONAGE_NUMBER_TYPE,
        "features": VONAGE_NUMBER_FEATURES,
    },
)

print(
    f'Here are {len(responseData["numbers"])} of the {responseData["count"]} matching numbers available for purchase:'
)

for number in responseData["numbers"]:
    print(f'Tel: {number["msisdn"]} Cost: {number["cost"]}')
