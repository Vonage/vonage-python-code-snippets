#!/usr/bin/env python3
import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')
VONAGE_APPLICATION_ID = os.getenv('VONAGE_APPLICATION_ID')

from vonage import Auth, Vonage
from vonage_application import (ApplicationConfig, ApplicationData,
                                ApplicationUrl, Messages, MessagesWebhooks)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

config = ApplicationConfig(
    name='My Renamed Application',
    capabilities=Messages(
        webhooks=MessagesWebhooks(
            inbound_url=ApplicationUrl(
                address='https://example.com/inbound_new_url', http_method='GET'
            ),
            status_url=ApplicationUrl(
                address='https://example.com/status_new_url', http_method='GET'
            ),
        ),
        authenticate_inbound_media=False,
    ),
)
response: ApplicationData = client.application.update_application(
    id=VONAGE_APPLICATION_ID, config=config
)

print(response)
