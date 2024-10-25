#!/usr/bin/env python3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

VONAGE_API_KEY = os.getenv('VONAGE_API_KEY')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET')

from vonage import Auth, Vonage
from vonage_application import (
    ApplicationConfig,
    ApplicationData,
    ApplicationUrl,
    Capabilities,
    Messages,
    MessagesWebhooks,
    Region,
    Verify,
    VerifyWebhooks,
    Voice,
    VoiceUrl,
    VoiceWebhooks,
)

client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_API_SECRET))

# Voice application options
voice = Voice(
    webhooks=VoiceWebhooks(
        answer_url=VoiceUrl(
            address='https://example.com/answer',
            http_method='POST',
            connect_timeout=500,
            socket_timeout=3000,
        ),
        fallback_answer_url=VoiceUrl(
            address='https://example.com/fallback',
            http_method='POST',
            connect_timeout=500,
            socket_timeout=3000,
        ),
        event_url=VoiceUrl(
            address='https://example.com/event',
            http_method='POST',
            connect_timeout=500,
            socket_timeout=3000,
        ),
    ),
    signed_callbacks=True,
    conversations_ttl=8000,
    leg_persistence_time=14,
    region=Region.NA_EAST,
)

# Messages application options
messages = Messages(
    version='v1',
    webhooks=MessagesWebhooks(
        inbound_url=ApplicationUrl(
            address='https://example.com/inbound', http_method='POST'
        ),
        status_url=ApplicationUrl(
            address='https://example.com/status', http_method='POST'
        ),
    ),
    authenticate_inbound_media=True,
)

# Verify application options
verify = Verify(
    webhooks=VerifyWebhooks(
        status_url=ApplicationUrl(address='https://example.com/status', http_method='GET')
    ),
)

# Set the application capabilities
capabilities = Capabilities(voice=voice, messages=messages, verify=verify)

# Set the application configuration that will be applied
params = ApplicationConfig(
    name='My Custom Application',
    capabilities=capabilities,
)

# Call the API
response: ApplicationData = client.application.create_application(params)

print(response)
