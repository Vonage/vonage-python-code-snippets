#!/usr/bin/env python3
import vonage, os
from dotenv import load_dotenv
from pprint import pprint

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

NEXMO_API_KEY = os.getenv('NEXMO_API_KEY')
NEXMO_API_SECRET = os.getenv('NEXMO_API_SECRET')

client = vonage.Client(
    key=NEXMO_API_KEY,
    secret=NEXMO_API_SECRET
)

response = client.application_v2.list_applications()

pprint(response)
