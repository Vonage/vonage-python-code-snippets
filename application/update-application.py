#!/usr/bin/env python3
import nexmo
from pprint import pprint

client = nexmo.Client(
    key=NEXMO_API_KEY,
    secret=NEXMO_API_SECRET
)

response = client.application_v2.update_application(NEXMO_APPLICATION_ID, {
  "name": "Python Update App",
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
    },
    "voice": {
      "webhooks": {
        "answer_url": {
          "address": "https://example.com/webhooks/answer",
          "http_method": "POST"
        },
        "event_url": {
          "address": "https://example.com/webhooks/event",
          "http_method": "POST"
        }
      }
    },
    "rtc": {
      "webhooks": {
        "event_url": {
          "address": "https://example.com/webhooks/event",
          "http_method": "POST"
        }
      }
    },
    "vbc": {}
  }
})

pprint(response)
