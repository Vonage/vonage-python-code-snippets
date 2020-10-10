#!/usr/bin/env python3
import os
from os.path import join, dirname
from pprint import pprint
from dotenv import load_dotenv
import vonage


dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

client = vonage.Client(
    key=VONAGE_API_KEY,
    secret=VONAGE_API_SECRET
)

response = client.application_v2.list_applications()

pprint(response)
