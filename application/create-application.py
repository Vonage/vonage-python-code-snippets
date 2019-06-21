#!/usr/bin/env python3
import nexmo
from pprint import pprint

client = nexmo.Client(
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
