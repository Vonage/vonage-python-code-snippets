#!/usr/bin/env python3
import vonage, os
from pprint import pprint

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

response = client.application_v2.list_applications()

pprint(response)
