import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
NUMBER_COUNTRY_CODE = os.getenv("NUMBER_COUNTRY_CODE")
NUMBER_TYPE = os.getenv("NUMBER_TYPE")
NUMBER_FEATURES = os.getenv("NUMBER_FEATURES")
NUMBER_SEARCH_CRITERIA = os.getenv("NUMBER_SEARCH_CRITERIA")
NUMBER_SEARCH_PATTERN = os.getenv("NUMBER_SEARCH_PATTERN")

from vonage import Auth, Vonage
from vonage_numbers import SearchAvailableNumbersFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

numbers, count, next = client.numbers.search_available_numbers(
    SearchAvailableNumbersFilter(
        country=NUMBER_COUNTRY_CODE,
        size=3,
        pattern=NUMBER_SEARCH_CRITERIA,
        search_pattern=NUMBER_SEARCH_PATTERN,
        type=NUMBER_TYPE,
        features=NUMBER_FEATURES,
    )
)
pprint(numbers)
print(count)
print(next)

for number in numbers:
    print(f'Tel: {number.msisdn} Cost: {number.cost}')
