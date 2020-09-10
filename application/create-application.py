#!/usr/bin/env python3
import vonage, os
from pprint import pprint

VONAGE_API_KEY = os.getenv("VONAGE_API_KEY")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

response = client.application_v2.create_application(
    {
        "name": "Code Example App",
        "capabilities": {
            "messages": {
                "webhooks": {
                    "inbound_url": {
                        "address": "https://example.com/webhooks/inbound",
                        "http_method": "POST",
                    },
                    "status_url": {
                        "address": "https://example.com/webhooks/status",
                        "http_method": "POST",
                    },
                }
            }
        },
    }
)

pprint(response)
