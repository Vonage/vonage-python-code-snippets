import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
NUMBER_SEARCH_CRITERIA = os.getenv("NUMBER_SEARCH_CRITERIA")
NUMBER_SEARCH_PATTERN = os.getenv("NUMBER_SEARCH_PATTERN")

import vonage

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

responseData = client.get_account_numbers(
    {"pattern": NUMBER_SEARCH_CRITERIA, "search_pattern": NUMBER_SEARCH_PATTERN}
)

print(
    f'Here are {len(responseData["numbers"])} of the {responseData["count"]} matching numbers in your account:'
)

for number in responseData["numbers"]:
    print(f'Tel: {number["msisdn"]} Type: {number["type"]}')
