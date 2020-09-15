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

response = client.application_v2.create_application({
    "name": "Code Example App",
    "capabilities": {
        "messages": {
            "webhooks": {
                "inbound_url": {
                    "address": "https://example.com/webhooks/inbound",
                    "http_method": "POST"
                },
                "status_url": {
                    "address": "https://example.com/webhooks/status",
                    "http_method": "POST"
                }
            }
        }
    }
})

pprint(response)
