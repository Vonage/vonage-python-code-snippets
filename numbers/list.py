import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")
NUMBER_SEARCH_CRITERIA = os.getenv("NUMBER_SEARCH_CRITERIA")
NUMBER_SEARCH_PATTERN = os.getenv("NUMBER_SEARCH_PATTERN")

import nexmo

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

responseData = client.get_account_numbers(
    {"pattern": NUMBER_SEARCH_CRITERIA, "search_pattern": NUMBER_SEARCH_PATTERN}
)

print(
    f'Here are {str(len(responseData["numbers"]))} of the {str(responseData["count"])} matching numbers in your account:'
)

for number in responseData["numbers"]:
    print(f'Tel: {number["msisdn"]} Type: {number["type"]}')
