import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")
COUNTRY_CODE = os.getenv("COUNTRY_CODE")
VONAGE_NUMBER_TYPE = os.getenv("VONAGE_NUMBER_TYPE")
VONAGE_NUMBER_FEATURES = os.getenv("VONAGE_NUMBER_FEATURES")

from vonage import Auth, Vonage
from vonage_numbers import SearchAvailableNumbersFilter

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

numbers, count, next = client.numbers.search_available_numbers(
    SearchAvailableNumbersFilter(
        country=COUNTRY_CODE,
        size=3,
        pattern='44701',
        search_pattern=1,
        type=VONAGE_NUMBER_TYPE,
        features=VONAGE_NUMBER_FEATURES,
    )
)
pprint(numbers)
print(count)
print(next)

for number in numbers:
    print(f'Tel: {number.msisdn} Cost: {number.cost}')
