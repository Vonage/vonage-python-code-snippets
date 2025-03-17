import os
from os.path import dirname, join
from pprint import pprint

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
NUMBER_SEARCH_CRITERIA = os.getenv("NUMBER_SEARCH_CRITERIA")
NUMBER_SEARCH_PATTERN = os.getenv("NUMBER_SEARCH_PATTERN")

from vonage import Auth, Vonage
from vonage_numbers import ListOwnedNumbersFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

numbers, count, next = client.numbers.list_owned_numbers(
    ListOwnedNumbersFilter(
        pattern=NUMBER_SEARCH_CRITERIA, search_pattern=NUMBER_SEARCH_PATTERN
    )
)

pprint(numbers)
print(count)
print(next)
